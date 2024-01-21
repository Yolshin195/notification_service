from logging import getLogger
from datetime import datetime
from uuid import UUID
from celery import shared_task, Task

from notification.message_sender_api import message_sender_api, MessageSenderApiException
from notification.models import Dispatch, MessageStatusReference, MessageStatusEnum, Client, Message

logger = getLogger(__name__)


@shared_task
def task_create_messages(dispatch_id: UUID):
    """
    Create messages for a given dispatch and initiate the message sending task for each client.

    :param dispatch_id: UUID - Identifier of the dispatch.
    """
    dispatch = Dispatch.objects.get(id=dispatch_id)
    status = MessageStatusReference.objects.get(code=MessageStatusEnum.CREATED.value)
    clients = Client.objects.filter(tag__id=dispatch.filter_tag.id,
                                    mobile_operator_code__id=dispatch.filter_mobile_operator_code.id)
    for client in clients:
        logger.info(f"task_create_messages: Creating message for client: {client}")
        message = Message.objects.create(client=client, dispatch=dispatch, status=status)
        task_send_message.apply_async(args=[message.id])
        logger.info(f"task_create_messages: Send message task initiated for client: {client}")

    logger.info("task_create_messages: Task completed successfully.")


@shared_task(bind=True, max_retries=10)
def task_send_message(self: Task, message_id: UUID):
    """
    Send a message to a client and handle errors, updating the message status as necessary.

    :param self: Task - Reference to the current Celery task object.
    :param message_id: UUID - Identifier of the message.
    """
    message = Message.objects.get(id=message_id)
    if message.status.code == MessageStatusEnum.COMPLETED.value:
        logger.info("task_send_message: Message already sent. Skipping.")
        return
    if message.dispatch.end_datetime.astimezone(message.client.timezone) < datetime.now(message.client.timezone):
        logger.info("task_send_message: Message sending time has passed.")
        message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.TIMEOUT.value)
        message.save()
        return

    try:
        message_sender_api(id=message.message_id,
                           phone=int(message.client.phone_number),
                           text=message.dispatch.message_text)
        logger.info("task_send_message: Message sent successfully.")
    except MessageSenderApiException as exc:
        logger.error(f"task_send_message: Error sending message - {exc}")
        message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.ERROR.value)
        message.save()
        raise self.retry(exc=exc, countdown=self.request.retries * 60)

    message.status = MessageStatusReference.objects.get(code=MessageStatusEnum.COMPLETED.value)
    message.save()
    logger.info("task_send_message: Task completed successfully.")
