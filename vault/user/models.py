from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtended(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    picture = models.ImageField(null=True, blank=True, upload_to='avatar_photos/', default="default-avatar.png")

class Photo(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='avatar_photos/', default="default-avatar.png")
    photo_id = models.ForeignKey(UserExtended, on_delete=models.CASCADE, null=True, blank=True)
