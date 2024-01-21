from uuid import UUID

from django.db.models import Count, Q

from notification.models import Dispatch, MessageStatusEnum


def build_dispatch_report(dispatch_id: UUID):
    return Dispatch.objects.filter(id=dispatch_id).values(
        'id',
        'start_datetime',
        'end_datetime',
        'message_text',
        'filter_mobile_operator_code__code',
        'filter_tag__code'
    ).annotate(
        created=Count('message', filter=Q(message__status__code=MessageStatusEnum.CREATED.value)),
        completed=Count('message', filter=Q(message__status__code=MessageStatusEnum.COMPLETED.value)),
        error=Count('message', filter=Q(message__status__code=MessageStatusEnum.ERROR.value)),
        timeout=Count('message', filter=Q(message__status__code=MessageStatusEnum.TIMEOUT.value))
    ).first()


def build_dispatch_reports():
    return Dispatch.objects.values(
        'id',
        'start_datetime',
        'end_datetime',
        'message_text',
        'filter_mobile_operator_code__code',
        'filter_tag__code'
    ).annotate(
        created=Count('message', filter=Q(message__status__code=MessageStatusEnum.CREATED.value)),
        completed=Count('message', filter=Q(message__status__code=MessageStatusEnum.COMPLETED.value)),
        error=Count('message', filter=Q(message__status__code=MessageStatusEnum.ERROR.value)),
        timeout=Count('message', filter=Q(message__status__code=MessageStatusEnum.TIMEOUT.value))
    ).order_by('id')
