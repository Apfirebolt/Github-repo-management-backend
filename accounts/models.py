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
    user = models.ForeignKey(UserModel, related_name='following', on_delete=models.CASCADE, null=True, blank=True)
    following = models.ForeignKey(UserModel, related_name='followed_by', on_delete=models.CASCADE, null=True, blank=True)
    following_since = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        unique_together = [['user', 'following']]

    def __str__(self):
        return str(self.user) + ' Follows ' + str(self.following)


class FriendRequests(models.Model):
    user_from = models.ForeignKey(UserModel, related_name='friend_request_from', on_delete=models.CASCADE, null=True, blank=True)
    user_to = models.ForeignKey(UserModel, related_name='friend_request_to', on_delete=models.CASCADE, null=True, blank=True)
    accepted = models.BooleanField(default=False)
    friend_since = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        unique_together = [['user_from', 'user_to']]

    def pre_save(self, request):
        self.user_from = request.user

    def __str__(self):
        return str(self.user_from) + ' - ' + str(self.user_to) + ' - ' + str(self.accepted)