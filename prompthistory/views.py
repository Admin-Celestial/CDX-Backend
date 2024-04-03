from django.http import JsonResponse
from .models import SmartqueryHistory
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated




class User_History(APIView):


    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def get(self, request, U_ID):
        try:
            data1 = SmartqueryHistory.objects.all().filter(U_ID=U_ID).order_by('-q_id').values()
            return JsonResponse(list(data1), safe=False)
        except Exception as e:
            return JsonResponse({"message": "An error occurred"}, status=500)
