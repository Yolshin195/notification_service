import logging

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from notification.models import Dispatch, Message
from notification.tasks import task_create_messages

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Dispatch)
def dispatch_post_save(sender, instance, **kwargs):
    task_create_messages.apply_async(args=[instance.id], eta=instance.start_datetime)


@receiver(pre_save, sender=Message)
def message_pre_save(sender, instance, **kwargs):
    if instance._state.adding:
        instance.message_id = Message.objects.count() + 1
