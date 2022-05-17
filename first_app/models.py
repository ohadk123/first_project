from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    profilePic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self) -> str:
        return self.user.username