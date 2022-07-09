from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
# default="Wef",


class Profile(models.Model):
    # first_name = models.CharField(max_length=50, blank=True, null=True)
    # last_name = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default="default.png", upload_to="profile_images")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

