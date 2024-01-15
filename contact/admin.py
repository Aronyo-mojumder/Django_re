from django.contrib import admin

# Register your models here.
from .models import Contact, Subscriber


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'message')


admin.site.register(Contact, ContactAdmin)


class SubsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
admin.site.register(Subscriber, SubsAdmin)
