from django.contrib import admin

from .models import Item, Sale, Client

# Register your models here.
admin.site.register(Item)
admin.site.register(Sale)
admin.site.register(Client)
