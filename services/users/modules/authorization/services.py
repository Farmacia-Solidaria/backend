import os
import jwt
import datetime

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from asgiref.sync import sync_to_async

from common.error.error import ActionError
from common.utils.information import get_private_key

from modules.authorization.forms import UserRegisterForm

@sync_to_async
def create_user(data):
    data['password1'] = data['password']
    data['password2'] = data['password']
    
    form = UserRegisterForm(data)
    if form.is_valid():
        form.save()
        return True
    
    return form.errors

@sync_to_async
def auth(data):
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60*int(os.environ["EXPIRATION_TIME"])),
            "permissions": [role.name for role in user.role_set.iterator()]
        }
        token = jwt.encode(payload, get_private_key(), 'RS256')
        
        return {
            "token": token
        }
    raise ActionError("Login not authorized")


@sync_to_async
def get_permissions(data):
    user = User.objects.get(username=data['username'])
    if user is not None:
        return {
            "permissions": [role.name for role in user.role_set.iterator()]
        }
    raise ActionError("User not found", )