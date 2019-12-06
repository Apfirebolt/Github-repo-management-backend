from rest_framework import serializers
from accounts.models import UserModel
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


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


    # Create passwords for users
    def validate_password(self, value):
        return make_password(value)

    def validate_first_name(self, value):
        return value.upper()
