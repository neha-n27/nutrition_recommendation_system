from django.urls import path
from . import views
urlpatterns=[
    path('yoga/',views.exercise_page,name='exercise_page'),
    path('yoga1/',views.yoga_page,name='yoga_page'),
    path('meditate/',views.meditation_page,name='meditation_page'),
    path('surya_namaskar/',views.surya_namaskar,name='surya_namaskar'),
    path('asana/',views.asana,name='asana'),
    
    ]