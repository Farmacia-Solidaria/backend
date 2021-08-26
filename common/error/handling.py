# from rest_framework.views import exception_handler
# from rest_framework.settings import api_settings
# from rest_framework import exceptions


# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)

#     # If unexpected error occurs (server error, etc.)
#     if response is None:
#         return response

#     response.data = "BIG ERROR"

#     return response