from django.core.exceptions import ValidationError
from django.db import models


class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    service_description = models.TextField()


def validate_image_size(image):
    width, height = image.width, image.height
    if width != 300 or height != 210:  # Corrected image size
        raise ValidationError(f'The image must be exactly 300x211 pixels. Current size is {width}x{height} pixels.')


class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='gallery/', validators=[validate_image_size])
    gallery_title = models.CharField(max_length=50)
    gallery_description = models.TextField()

    def __str__(self):
        return self.gallery_title


def Team_validate_image_size(image):
    width, height = image.width, image.height
    if width != 265 or height != 265:  # Corrected image size
        raise ValidationError(f'The image must be exactly 265x265 pixels. Current size is {width}x{height} pixels.')


class Team(models.Model):
    member_img = models.ImageField(upload_to='team/', validators=[Team_validate_image_size])
    member_title = models.CharField(max_length=50)
    member_description = models.TextField()
    facebook_link = models.TextField(blank=True, null=True)
    twitter_link = models.TextField(blank=True, null=True)
    whatsapp_link = models.TextField(blank=True, null=True)
    linkedin_link = models.TextField(blank=True, null=True)
    instagram_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.member_title
