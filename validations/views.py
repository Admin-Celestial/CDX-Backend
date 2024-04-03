from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Valids
from .models import Validation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required



class validator_v(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = Valids(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
#permission_classes = [IsAuthenticated]
@method_decorator(csrf_exempt)
def view_val(request):
    try:
        data = Validation.objects.all().values()
        return JsonResponse(list(data), safe=False)
    except Exception as e:
        return JsonResponse({"message": "An error occurred"}, status=500)



class ApproveDisapprove(APIView):


    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)

    def put(self, request, pk, format=None):
        try:
            valid_entry = Validation.objects.get(val_id=pk)
        except Validation.DoesNotExist:
            return Response({"message": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)

        status = request.data.get("status", None)

        if status is None:
            return Response({"message": "Missing 'status' field in request data"}, status=status.HTTP_400_BAD_REQUEST)

        if status == '0' or status == '1' or status is None:
            valid_entry.status = status
            valid_entry.save()
            if status == '0':
                status_message = "disapproved"
            elif status == '1':
                status_message = "approved"
            else:
                status_message = "not validated"
            return Response({"message": f"Entry {pk} is {status_message}.", "status": status})
        else:
            return Response({"message": "Invalid 'status' value"}, status=status.HTTP_400_BAD_REQUEST)
