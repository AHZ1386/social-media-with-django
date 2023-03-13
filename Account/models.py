from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='image',verbose_name='عکس پروفایل',blank=True)
    biography = models.CharField(max_length=110, verbose_name='بیوگرافی', blank=True)
    following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)
    def get_absolute_url(self):
        return '/'
    def get_model_fields(model):
        return model._meta.fields
    