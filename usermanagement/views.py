from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TempUserMasters
from .models import TempUserMaster
from rest_framework.response import Response
from rest_framework.response import Response

class TempUserMasterView(APIView):
    permission_classes = [IsAuthenticated]


    @method_decorator(csrf_exempt)
    def get(self, request, id=None, format=None):
        if id is not None:
            temp_user = get_object_or_404(TempUserMaster, id=id)
            serializer = TempUserMasters(temp_user)
            return Response(serializer.data)
        else:
            temp_users = TempUserMaster.objects.all()
            serializer = TempUserMasters(temp_users, many=True)
            return Response(serializer.data)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = TempUserMasters(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @method_decorator(csrf_exempt)
    def put(self, request, id, format=None):
        temp_user = get_object_or_404(TempUserMaster, id=id)
        serializer = TempUserMasters(temp_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def delete(self, request, id, format=None):
        temp_user = get_object_or_404(TempUserMaster, id= id)
        temp_user.delete()
        response_data = {
                'message': 'User account removed  successfully'
            }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
