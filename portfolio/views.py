from django.shortcuts import render

# Create your views here.

def portfolio(request):
    
    
    # get the profile
    profile = request.user.profile

    context={
        'profile': profile,
    }

    return render(request, 'portfolio/portfolio.html', context)