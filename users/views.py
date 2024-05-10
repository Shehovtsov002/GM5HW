import string
import random

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

from users.models import ConfirmationCode
from users.serializers import UserRegistrationSerializer, UserAuthorizationSerializer, ConfirmationCodeSerializer


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    user = User.objects.create_user(**serializer.validated_data, is_active=False)
    ConfirmationCode.objects.create_unique(user=user, confirmation_code=confirmation_code)
    return Response(data={'confirmation_code': confirmation_code}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthorizationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key})

    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('confirmation_code')
    try:
        user = ConfirmationCode.objects.get(confirmation_code=code).user
    except ConfirmationCode.DoesNotExist:
        return Response(data={'error': 'Invalid confirmation code'}, status=status.HTTP_404_NOT_FOUND)
    user.is_active = True
    user.save()
    return Response(data={'message': 'User successfully confirmed'})

