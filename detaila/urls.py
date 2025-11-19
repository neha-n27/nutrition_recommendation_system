from django.urls import path
from . import views

urlpatterns = [
    path('de/', views.home, name='home'),
    
    # Define other URLs specific to 'details' app here
]
