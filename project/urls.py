"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from detaila import views as detaila_views
from nutrition import views as nutrition_views
from recommendations import views as recommendations_views  # Fix typo here
# from recommendations.views import views as preference_view  # Ensure correct import
from yoga  import views as yoga_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('detaila/', include('detaila.urls')),
    path('faq/',detaila_views.faq_view,name='faq'),
    path('nutrition/', include('nutrition.urls')),
    path('recommendations/', include('recommendations.urls')),  # Ensure correct path
    path('yoga/', include('yoga.urls')),  # Ensure correct path

]

