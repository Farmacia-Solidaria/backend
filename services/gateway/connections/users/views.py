from django.http.response import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.kafka.send import send_and_wait_message

class UserViewset(APIView):

    def post(self, request, action):

            data = send_and_wait_message(
                service="users", 
                action=action, 
                data=request.data,
                filter=True,
                suppress_errors=True
            )
            
            return Response(data, status=status.HTTP_200_OK)