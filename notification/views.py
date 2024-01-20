from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    Client, Dispatch, Message,
    MobileOperatorCodeReference, MessageStatusReference, TagReference
)
from .serializers import (
    ClientSerializer, DispatchSerializer, MessageSerializer,
    MobileOperatorCodeReferenceSerializer, MessageStatusReferenceSerializer, TagReferenceSerializer
)


class MobileOperatorCodeReferenceViewSet(viewsets.ModelViewSet):
    queryset = MobileOperatorCodeReference.objects.all().order_by('id')
    serializer_class = MobileOperatorCodeReferenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code"]


class MessageStatusReferenceViewSet(viewsets.ModelViewSet):
    queryset = MessageStatusReference.objects.all().order_by('id')
    serializer_class = MessageStatusReferenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code"]


class TagReferenceViewSet(viewsets.ModelViewSet):
    queryset = TagReference.objects.all().order_by('id')
    serializer_class = TagReferenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code"]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer


class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all().order_by('id')
    serializer_class = DispatchSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer


class DispatchReportApiView(APIView):
    def get(self, request, format=None):
        return Response({'test': 'success!'})
