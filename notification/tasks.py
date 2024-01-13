from datetime import datetime
from uuid import UUID
from celery import shared_task

from notification.models import Dispatch, MessageStatusReference, MessageStatusEnum, Client, Message


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
        print("Уже поздно отправлять сообщение!!!")
        return
    if message.dispatch.start_datetime.astimezone(message.client.timezone) > datetime.now(message.client.timezone):
        print("Ещё рано отправлять сообщение!!!")
        return

    print("Сообщение отправлено!!!")

    message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.COMPLETED.value)
    message.save()
