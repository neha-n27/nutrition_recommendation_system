from django.urls import path
from .views import preference_view

urlpatterns = [
    path('recommendations/', preference_view, name='preferences'),
]
