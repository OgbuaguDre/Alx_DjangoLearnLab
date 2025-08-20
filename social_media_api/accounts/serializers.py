from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # make sure fields are explicitly defined when useful
    username = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    # use CharField for password (write_only so it won’t appear in responses)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # ensure password is hashed using create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # create token for authentication
        Token.objects.create(user=user)
        return user
