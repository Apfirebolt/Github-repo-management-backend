from rest_framework import serializers
from accounts.models import CustomUser,UserFollowing, FriendRequests
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': ('No account exists with these credentials, check password and email')
    }

    def validate(self, attrs):
        
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data 
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['id'] = self.user.id
        data['is_admin'] = self.user.is_superuser
        return data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        min_length=8,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    access = serializers.SerializerMethodField()
    refresh = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'id', 'is_staff', 'password', 'access', 'refresh',)
    
    def get_refresh(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh)

    def get_access(self, user):
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token),
        return access

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
        follow_obj = super(FollowSerializer, self).create(validated_data)
        follow_obj.user = CustomUser.objects.get(pk=19)
        follow_obj.following_since = timezone.now()
        follow_obj.save()
        return follow_obj


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequests
        fields = ('user_from', 'user_to',)


