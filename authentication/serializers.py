from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from authentication.models import User
from promise.models import Promise


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        email = data['email']
        users = User.objects.filter(email=email)

        if users:
            raise serializers.ValidationError(
                "A user with that email already exists."
            )

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(
        min_length=8,
        max_length=128,
        write_only=True
    )

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'Invalid username.'
            )

        if password is None:
            raise serializers.ValidationError(
                'Invalid password.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Invalid user.'
            )

        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)

        return {
            'token': token.key
        }


class UserSerializer(serializers.ModelSerializer):
    promises_as_inviter = serializers.PrimaryKeyRelatedField(source='user1', many=True, queryset=Promise.objects.all())
    promises_as_invitee = serializers.PrimaryKeyRelatedField(source='user2', many=True, queryset=Promise.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'promises_as_inviter', 'promises_as_invitee')
