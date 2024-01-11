from rest_framework import serializers
from .models import (
    Client, Dispatch, Message,
    MobileOperatorCodeReference, MessageStatusReference, TagReference
)


class MobileOperatorCodeReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileOperatorCodeReference
        fields = '__all__'


class MessageStatusReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageStatusReference
        fields = '__all__'


class TagReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagReference
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
