from django.http.response import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.kafka.send import send_and_wait_message

class UserViewset(APIView):

    def post(self, request, action):
        data = send_and_wait_message(
            service="users", 
            method="post",
            action=action, 
            data=request.data,
            filter=True,
            suppress_errors=True
        )
        
        if data:
            return Response(data, status=data["data"]["status"] if data["error"] else status.HTTP_200_OK)
        
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

    def get(self, request, action):
        data = send_and_wait_message(
            service="users", 
            method="get",
            action=action, 
            data=request.data,
            filter=True,
            suppress_errors=True
        )
        
        if data:
            return Response(data, status=data["data"]["status"] if data["error"] else status.HTTP_200_OK)
        
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)

    def delete(self, request, action):
        data = send_and_wait_message(
            service="users", 
            method="delete",
            action=action, 
            data=request.data,
            filter=True,
            suppress_errors=True
        )
        
        if data:
            return Response(data, status=data["data"]["status"] if data["error"] else status.HTTP_200_OK)
        
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)