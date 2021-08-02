from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

import requests

class LoginViewset(APIView):

    def get(self, request):
        return Response(requests.get("http://login:8002"))