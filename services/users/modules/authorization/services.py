from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from asgiref.sync import sync_to_async

@sync_to_async
def create_user(data):
    data['password1'] = data['password']
    data['password2'] = data['password']
    
    form = UserCreationForm(data)
    if form.is_valid():
        form.save()
        return True
    
    return form.errors
