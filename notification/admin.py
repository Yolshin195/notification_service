from django.contrib import admin
from .models import (
    Client, Dispatch, Message,
    MobileOperatorCodeReference, MessageStatusReference, TagReference
)

admin.site.register(Client)
admin.site.register(Dispatch)
admin.site.register(Message)

admin.site.register(MobileOperatorCodeReference)
admin.site.register(MessageStatusReference)
admin.site.register(TagReference)
