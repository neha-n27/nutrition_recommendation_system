from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'detaila/home.html')

def faq_view(request):
    return render(request, 'detaila/faq.html')