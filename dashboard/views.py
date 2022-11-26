from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#import messages
from django.contrib import messages

# Create your views here.

@login_required(login_url="/login/")
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def logoutpg(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("")