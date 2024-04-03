from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
import logging

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        

        return token
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['POST'])
@parser_classes([JSONParser])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = get_user_model().objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data['email'],
            status_toggle=request.data.get('status_toggle', False)  
        )
        refresh = RefreshToken.for_user(user)
        return Response({'message': 'Account Created Successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    refresh_token = request.data.get('refresh_token')

    if not refresh_token:
        return Response({'error': 'refresh_token parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        RefreshToken(refresh_token).blacklist()
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)

'''
class LogTestAPI(APIView):
    @method_decorator(csrf_exempt)
    def get(self, request):


        db_logger = logging.getLogger('db')

        db_logger.info('info message')
        db_logger.warning('warning message')

        try:
            1/0
        except Exception as e:
            db_logger.exception(e)


        print('Log test')
        return Response({'data': True}, status=status.HTTP_200_OK)
'''
