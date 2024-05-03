from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from users.models import ConfirmationCode


class ConfirmationCodeSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(max_length=6, min_length=6)

    def validate_confirmation_code(self, confirmation_code):
        try:
            ConfirmationCode.objects.get(confirmation_code=confirmation_code)
        except ConfirmationCode.DoesNotExist:
            raise ValidationError('Confirmation code does not exist')
        return confirmation_code


class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Username already exists')
