from datetime import datetime, UTC
import logging

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from notification.models import Dispatch, Message, MessageIdTable
from notification.tasks import task_create_messages

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Dispatch)
def dispatch_post_save(sender, instance, **kwargs):
    eta = instance.start_datetime.replace(tzinfo=instance.timezone).astimezone(UTC)
    logger.warning(
        f"dispatch_post_save: datetime start: {eta}, datetime now: {datetime.now(UTC)}"
    )
    task_create_messages.apply_async(args=[instance.id], eta=eta)
