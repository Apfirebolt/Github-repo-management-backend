from rest_framework import serializers
from accounts.models import UserModel,UserFollowing, FriendRequests
from rest_framework.validators import UniqueValidator
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=UserModel.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=UserModel.objects.all())])
    password = serializers.CharField(
          write_only=True,
          required=True,
          help_text='Leave empty if no change needed',
          style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password',
              'profile_image', 'about_me',)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_first_name(self, value):
        return value.upper()


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ('id', 'user', 'following', 'following_since',)
        extra_kwargs = {'following_since': {'read_only': True},
                        'user': {'read_only': True, 'required': False},
                        'id': {'read_only': True}
                        }

    def create(self, validated_data):
        follow_obj = super(FollowSerializer, self).create(validated_data)
        follow_obj.user = UserModel.objects.get(pk=self.context['request'].user.id)
        follow_obj.following_since = timezone.now()
        follow_obj.save()
        return follow_obj


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequests
        fields = ('id', 'user_from', 'user_to', 'accepted', )

    extra_kwargs = {
                    'user_from': {'read_only': True, 'required': False},
                    'id': {'read_only': True},
                    'accepted': {'read_only': True}
                    }

    def create(self, validated_data):
        friend_obj = super(FriendSerializer, self).create(validated_data)
        friend_obj.user_from = UserModel.objects.get(pk=self.context['request'].user.id)
        friend_obj.save()
        return friend_obj

    def update(self, instance, validated_data):
        instance = super(FriendSerializer, self).update(instance, validated_data)
        return instance


