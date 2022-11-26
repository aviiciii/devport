from django.shortcuts import render, redirect
from dev_db.models import Profile
from django.contrib.auth.decorators import login_required
from DevPort.settings import LOGIN_REDIRECT_URL
from django.contrib import messages

# Create your views here.

@login_required(login_url=LOGIN_REDIRECT_URL)
def portfolio(request):
    # get the profile
    profile = request.user.profile
    context={
        'profile': profile,
    }
    return render(request, 'portfolio/portfolio.html', context)


def portfolio_public(request, profile_id):
    # get the profile
    try:
        profile = Profile.objects.get(pk=profile_id)
        context={
            'profile': profile,
        }
    except:
        messages.error(request, "Portfolio not found!")
        return redirect("index")

    return render(request, 'portfolio/portfolio.html', context)
