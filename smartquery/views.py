from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from .models import ChatHistory
from .serializers import historys
from smartquery.text import generate_text
import json


@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def generate_response(request):
    
    #tokenizer, model = load_model()
    request_body = json.loads(request.body)
    question = request_body.get('Question')
    U_ID = request_body.get('U_ID')

    #en = Final(question = request_body.get('Question'))
    #en.save()


    
    response = generate_text(question)
    generated_response = ChatHistory(question = question,response = response, U_ID = U_ID)
    generated_response.save()    
    #ea = Final(response = generate_text(question))
    #ea.save()
    
    #ea = Final(generate_text(question))
    #ea.save()
    #response = ea




# prompt = request.GET.get('prompt', '')
    # response = f'LLM generated response for: "{pr}"'
    return JsonResponse({'response': response})



class LikedDisliked(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        try:
            history_entry = ChatHistory.objects.get(q_id=pk)
        except ChatHistory.DoesNotExist:
            return Response({"message": "Entry not found"}, status=status.HTTP_404_NOT_FOUND)

        status = request.data.get("status", None)

        if status is None:
            return Response({"message": "Missing 'status' field in request data"}, status=status.HTTP_400_BAD_REQUEST)

        if status == '0' or status == '1' or status is None:
            history_entry.status = status
            history_entry.save()
            if status == '0':
                status_message = "Dis-liked"
            elif status == '1':
                status_message = "approved"
            else:
                status_message = "Liked"
            return Response({"message": f"Entry {pk} is {status_message}.", "status": status})
        else:
            return Response({"message": "Invalid 'status' value"}, status=status.HTTP_400_BAD_REQUEST)
