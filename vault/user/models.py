from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtended(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField()
    picture = models.ImageField(null=True, blank=True, upload_to='avatar_photos/', default="default-avatar.jpg")

class Photo(models.Model):
    photo = models.ImageField(upload_to='images/')
    title = models.CharField(null=True, blank=True, max_length=30, default="Photo")
    description = models.TextField(null=True, blank=True)
    photo_id = models.ForeignKey(UserExtended, on_delete=models.CASCADE, null=True, blank=True)
