from django.contrib import admin
from . models import CustomUser, FriendRequests, UserFollowing
from django.contrib.admin import ModelAdmin


class UserAdminManager(ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'last_login',)
    list_filter = ('is_staff',)


class FriendRequestManager(ModelAdmin):
    list_display = ('user_from', 'user_to', 'accepted',)
    list_filter = ('accepted',)


class FollowingModel(ModelAdmin):
    list_display = ('user', 'following', 'following_since',)


admin.site.register(CustomUser, UserAdminManager)
admin.site.register(FriendRequests, FriendRequestManager)
admin.site.register(UserFollowing, FollowingModel)

