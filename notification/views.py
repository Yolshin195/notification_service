from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from .models import (
    Client,
    Dispatch,
    Message,
    MobileOperatorCodeReference,
    MessageStatusReference,
    TagReference,
)
from .reports import build_dispatch_report, build_dispatch_reports
from .serializers import (
    ClientSerializer,
    DispatchSerializer,
    MessageSerializer,
    MobileOperatorCodeReferenceSerializer,
    MessageStatusReferenceSerializer,
    TagReferenceSerializer,
    DispatchReportSerializer,
)


class MobileOperatorCodeReferenceViewSet(viewsets.ModelViewSet):
    queryset = MobileOperatorCodeReference.objects.all().order_by("id")
    serializer_class = MobileOperatorCodeReferenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code"]


class MessageStatusReferenceViewSet(viewsets.ModelViewSet):
    queryset = MessageStatusReference.objects.all().order_by("id")
    serializer_class = MessageStatusReferenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code"]


class TagReferenceViewSet(viewsets.ModelViewSet):
    queryset = TagReference.objects.all().order_by("id")
    serializer_class = TagReferenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["code"]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("id")
    serializer_class = ClientSerializer


class DispatchViewSet(viewsets.ModelViewSet):
    queryset = Dispatch.objects.all().order_by("id")
    serializer_class = DispatchSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by("id")
    serializer_class = MessageSerializer


class DispatchReportViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        report = build_dispatch_report(pk)
        serializer = DispatchReportSerializer(report)
        return Response(serializer.data)

    def list(self, request):
        reports = build_dispatch_reports()
        serializer = DispatchReportSerializer(reports, many=True)
        return Response(serializer.data)
