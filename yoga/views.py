from django.shortcuts import render

# Create your views here.
def exercise_page(request):
    return render(request,'exercise_page.html')
def yoga_page(request):
    return render (request,'yoga_page.html')
def meditation_page(request):
    return render(request,'meditation_page.html')
def surya_namaskar(request):
    return render(request,'surya_namaskar.html')
def asana(request):
    return render(request,'asana.html')