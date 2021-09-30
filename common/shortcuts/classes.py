from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.kafka.send import send_and_wait_message

class SimpleConnection(APIView):

    def __init__(self, name=None):
        className = self.__class__.__name__.lower().split("connection")[0]
        self.name = className if name is None else name 


    def _default_send_routine(self, method: str, request: HttpRequest, action: str):

        token = request.headers.get("Authorization") or ""

        data = send_and_wait_message(
            service=self.name, 
            method=method,
            action=action, 
            data=request.data,
            filter=True,
            suppress_errors=True,
            token=token
        )
        
        if data:
            return Response(data, status=data["data"]["status"] if data["error"] else status.HTTP_200_OK)
        
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


    def post(self, request, action): return self._default_send_routine('post', request, action)
    def get(self, request, action): return self._default_send_routine( 'get', request, action)
    def put(self, request, action): return self._default_send_routine('put', request, action)
    def patch(self, request, action): return self._default_send_routine('patch', request, action)
    def delete(self, request, action): return self._default_send_routine('delete', request, action)
    def options(self, request, action): return self._default_send_routine('options', request, action)
    def head(self, request, action): return self._default_send_routine('head', request, action)