import uuid
from enum import Enum

from django.db import models
from timezone_field import TimeZoneField


class MessageStatusEnum(Enum):
    CREATED = "created"
    COMPLETED = "completed"
    ERROR = "error"


class BaseEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.id}"


class BaseReference(BaseEntity):
    code = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.name} ({self.code})"


class TagReference(BaseReference):
    pass


class MessageStatusReference(BaseReference):
    pass


class MobileOperatorCodeReference(BaseReference):
    pass


class Client(BaseEntity):
    phone_number = models.CharField(max_length=11, unique=True)
    mobile_operator_code = models.ForeignKey(MobileOperatorCodeReference, on_delete=models.CASCADE)
    tag = models.ForeignKey(TagReference, on_delete=models.CASCADE)
    timezone = TimeZoneField(choices_display="WITH_GMT_OFFSET")

    def __str__(self):
        return f"{self.__class__.__name__} - {self.phone_number}"


class Dispatch(BaseEntity):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message_text = models.TextField()
    filter_mobile_operator_code = models.ForeignKey(MobileOperatorCodeReference, on_delete=models.CASCADE)
    filter_tag = models.ForeignKey(TagReference, on_delete=models.CASCADE)


class Message(BaseEntity):
    message_id = models.IntegerField(unique=True, editable=False)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(MessageStatusReference, on_delete=models.CASCADE)
    dispatch = models.ForeignKey(Dispatch, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
