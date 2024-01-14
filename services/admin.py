from django.contrib import admin
from services.models import Service, Gallery, Team


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("service_icon", 'service_name', 'service_description')


admin.site.register(Service, ServiceAdmin)


class GalleryAdmin(admin.ModelAdmin):  # Fixed the class name
    list_display = ("gallery_img", 'gallery_title', 'gallery_description')


admin.site.register(Gallery, GalleryAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "member_img",
        "member_title",
        "member_description",
        "facebook_link",
        "twitter_link",
        "whatsapp_link",
        "linkedin_link",
        "instagram_link",
    )


admin.site.register(Team, TeamAdmin)
