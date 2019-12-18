from django.db import models
from django.contrib.auth.models import AbstractUser
from django_github import settings


class UserModel(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_pics', default='1.png', blank=True)
    about_me = models.TextField(max_length=500, blank=True)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.username)


class UserFollowing(models.Model):
    user = models.ForeignKey(UserModel, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(UserModel, related_name='followed_by', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' Follows ' + str(self.following)