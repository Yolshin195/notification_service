from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientViewSet,
    DispatchViewSet,
    MessageViewSet,
    MobileOperatorCodeReferenceViewSet,
    MessageStatusReferenceViewSet,
    TagReferenceViewSet,
    DispatchReportViewSet,
)

router = DefaultRouter()
router.register(r"dispatch-reports", DispatchReportViewSet, basename="dispatch-reports")
router.register(r"clients", ClientViewSet)
router.register(r"dispatches", DispatchViewSet)
router.register(r"messages", MessageViewSet)
router.register(r"mobile-operator-codes", MobileOperatorCodeReferenceViewSet)
router.register(r"message-statuses", MessageStatusReferenceViewSet)
router.register(r"tags", TagReferenceViewSet)

urlpatterns = [path("", include(router.urls))]
