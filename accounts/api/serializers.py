from rest_framework import serializers
from accounts.models import CustomUser,UserFollowing, FriendRequests
from rest_framework.validators import UniqueValidator
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(
          write_only=True,
          required=True,
          help_text='Leave empty if no change needed',
          style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ('user', 'following', 'following_since',)
        extra_kwargs = {'following_since': {'read_only': True},
                        'user': {'read_only': True, 'required': False},
                        }

    def create(self, validated_data):
        print('Inside the create method : ', self.context['request'].user, validated_data)
        follow_obj = super(FollowSerializer, self).create(validated_data)
        follow_obj.user = CustomUser.objects.get(pk=19)
        follow_obj.following_since = timezone.now()
        follow_obj.save()
        return follow_obj


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequests
        fields = ('user_from', 'user_to',)


