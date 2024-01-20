from logging import getLogger
from datetime import datetime
from uuid import UUID
from celery import shared_task

from notification.message_sender_api import message_sender_api
from notification.models import Dispatch, MessageStatusReference, MessageStatusEnum, Client, Message

logger = getLogger(__name__)


@shared_task
def task_create_messages(dispatch_id: UUID):
    dispatch = Dispatch.objects.get(id=dispatch_id)
    status = MessageStatusReference.objects.get(code=MessageStatusEnum.CREATED.value)
    clients = Client.objects.filter(tag__id=dispatch.filter_tag.id,
                                    mobile_operator_code__id=dispatch.filter_mobile_operator_code.id)
    for client in clients:
        message = Message.objects.create(client=client, dispatch=dispatch, status=status)
        task_send_message.apply_async(args=[message.id])


@shared_task
def task_send_message(message_id: UUID):
    message = Message.objects.get(id=message_id)
    if message.status.code == MessageStatusEnum.COMPLETED.value:
        return
    if message.dispatch.end_datetime.astimezone(message.client.timezone) < datetime.now(message.client.timezone):
        logger.info("Уже поздно отправлять сообщение!!!")
        return
    if message.dispatch.start_datetime.astimezone(message.client.timezone) > datetime.now(message.client.timezone):
        logger.info("Ещё рано отправлять сообщение!!!")
        return

    if message_sender_api(id=message.message_id,
                          phone=int(message.client.phone_number),
                          text=message.dispatch.message_text):
        logger.info("Сообщение отправлено!!!")
        message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.COMPLETED.value)
        message.save()
    else:
        message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.ERROR.value)
        message.save()
