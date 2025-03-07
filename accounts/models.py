from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django_github import settings


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Email", unique=True, max_length=255)
    username = models.CharField("User Name", unique=True, max_length=255, blank=True, null=True)
    firstName = models.CharField("First Name", max_length=100, blank=True, null=True)
    lastName = models.CharField("Last Name", max_length=100, blank=True, null=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff', default=False)
    is_superuser = models.BooleanField('Super User', default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        '''Doc string for meta'''
        verbose_name_plural = "User"


class UserFollowing(models.Model):
    user = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE, null=True, blank=True)
    following = models.ForeignKey(CustomUser, related_name='followed_by', on_delete=models.CASCADE, null=True, blank=True)
    following_since = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.user) + ' Follows ' + str(self.following)


class FriendRequests(models.Model):
    user_from = models.ForeignKey(CustomUser, related_name='friend_request_from', on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser, related_name='friend_request_to', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    friend_since = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.user_from) + ' - ' + str(self.following) + ' - ' + str(self.accepted)