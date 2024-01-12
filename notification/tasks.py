from datetime import datetime
from uuid import UUID
from celery import shared_task

from notification.models import Dispatch, MessageStatusReference, MessageStatusEnum, Client, Message


@shared_task
def task_create_messages(dispatch_id: UUID):
    dispatch = Dispatch.objects.get(id=dispatch_id)
    status = MessageStatusReference.objects.get(code=MessageStatusEnum.CREATED)
    for client in Client.objects.filter(dispatch.filter_tag, dispatch.filter_mobile_operator_code):
        message = Message.objects.create(client=client, dispatch=dispatch, status=status)
        task_send_message.apply_async(args=[message.id])


@shared_task
def task_send_message(message_id: UUID):
    message = Message.objects.get(id=message_id)
    if message.status.code == MessageStatusEnum.COMPLETED.value:
        return
    if message.dispatch.end_datetime < datetime.now():
        return
    if message.dispatch.start_datetime > datetime.now():
        return

    print("Сообщение отправлено!!!")

    message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.COMPLETED)
    message.save()
