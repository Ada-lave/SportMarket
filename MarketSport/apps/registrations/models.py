from django.db import models
from django.contrib.auth.models import User
import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=60)
    img = models.ImageField(null=True, blank=True)


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



    def __str__(self):
        return self.user.username
