from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def chemnitz(request):
    return render(request, 'chemnitz.html')

def tuchemnitz(request):
    return render(request, 'tuchemnitz.html')

def dormitory(request):
    return render(request, 'dormitory.html')

def contact(request):
    return render(request, 'contactus.html')

def news(request):
    return render(request, 'news.html')

def conversations(request):
    return render(request, 'conversations.html')