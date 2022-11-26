from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:profile_id>', views.portfolio_public, name='portfolio_public'),
]