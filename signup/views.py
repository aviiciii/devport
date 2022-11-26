import uuid
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.

def signup(request):
    if request.method == 'POST':
        id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password2']
        
        #create user
    
        if password == password1:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken') 
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    return render(request, 'signup/signup.html')