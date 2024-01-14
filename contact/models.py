from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=100,blank=True, null=True)
    # Example field for phone number
    message = models.TextField()

    def __str__(self):
        return self.name