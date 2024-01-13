import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from notification.models import Dispatch
from notification.tasks import task_create_messages

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Dispatch)
def dispatch_pre_save(sender, instance, **kwargs):
    task_create_messages.apply_async(args=[instance.id])
