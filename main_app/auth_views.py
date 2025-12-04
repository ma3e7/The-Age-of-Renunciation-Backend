from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import GameUser

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    name = request.data.get('name')
    password = request.data.get('password')

    if not name or not password:
        return Response({"error": "name and password required"}, status=status.HTTP_400_BAD_REQUEST)

    if GameUser.objects.filter(name=name).exists():
        return Response({"error": "User exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = GameUser.objects.create_user(name=name, password=password)
    tokens = get_tokens_for_user(user)
    return Response(tokens, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    name = request.data.get('name')
    password = request.data.get('password')
    user = authenticate(name=name, password=password)
    if not user:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    tokens = get_tokens_for_user(user)
    return Response(tokens, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def signout(request):
    return Response({"message": "Client should remove tokens to sign out."})
