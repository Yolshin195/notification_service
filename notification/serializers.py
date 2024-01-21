from django.core.validators import RegexValidator
from rest_framework import serializers
from .utils import TimeZoneSerializerChoiceField
from .models import (
    Client,
    Dispatch,
    Message,
    MobileOperatorCodeReference,
    MessageStatusReference,
    TagReference,
)


class MobileOperatorCodeReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileOperatorCodeReference
        fields = "__all__"


class MessageStatusReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageStatusReference
        fields = "__all__"


class TagReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagReference
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    timezone = TimeZoneSerializerChoiceField()
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^7\d{10}$',
                message='Неверный формат номера телефона. Используйте формат 7XXXXXXXXXX.'
            )
        ]
    )

    class Meta:
        model = Client
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class DispatchSerializer(serializers.ModelSerializer):
    timezone = TimeZoneSerializerChoiceField()

    class Meta:
        model = Dispatch
        fields = "__all__"


class DispatchReportSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    start_datetime = serializers.DateTimeField()
    end_datetime = serializers.DateTimeField()
    message_text = serializers.CharField()
    filter_mobile_operator_code__code = serializers.CharField()
    filter_tag__code = serializers.CharField()
    created = serializers.IntegerField()
    completed = serializers.IntegerField()
    error = serializers.IntegerField()
    timeout = serializers.IntegerField()
