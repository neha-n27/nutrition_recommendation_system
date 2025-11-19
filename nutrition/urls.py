from django.urls import path
from . import views

urlpatterns = [
    path('nutrients/', views.food_nutrient_view, name='food_nutrient_view'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
]
