from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from DevPort.settings import LOGIN_REDIRECT_URL
#import messages
from django.contrib import messages

# Create your views here.
@login_required(login_url=LOGIN_REDIRECT_URL)
def logoutpg(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("")


@login_required(login_url=LOGIN_REDIRECT_URL)
def dashboard(request):
    if request.method == "POST":
        # get the form data
        name= request.POST.get('name')
        role = request.POST.get('role')
        about = request.POST.get('about')
        college = request.POST.get('college')
        course = request.POST.get('course')
        grade = request.POST.get('grade')
        graduationyear = request.POST.get('graduationyear')
        contactemail = request.POST.get('contactemail')
        instagram= request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        github = request.POST.get('github')
        linkedin = request.POST.get('linkedin')

        # check if user has profile
        if request.user.profile:
            # update
            profile = request.user.profile
            profile.name = name
            profile.role = role
            profile.about = about
            profile.college = college
            profile.course = course
            profile.grade = grade
            profile.graduationyear = graduationyear
            profile.contactemail = contactemail
            profile.instagram = instagram
            profile.twitter = twitter
            profile.github = github
            profile.linkedin = linkedin
            profile.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("dashboard")
        
    return render(request, 'dashboard/dashboard.html')




