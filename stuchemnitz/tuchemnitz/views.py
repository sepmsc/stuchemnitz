from django.shortcuts import render
# from tuchemnitz.forms import SubmitForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def chemnitz(request):
    return render(request, 'stadtChemnitz.html')

def tuchemnitz(request):
    return render(request, 'tchemnitz.html')

def dormitory(request):
    return render(request, 'dormitory.html')

def contact(request):
    return render(request, 'contactus.html')

def news(request):
    return render(request, 'news.html')

def conversations(request):
    return render(request, 'conversations.html')

def submitview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        request.save()
        return render(request, 'submit.html', {'name': name, 'email': email, 'comment': comment})
    