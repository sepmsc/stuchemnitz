from django.shortcuts import render, redirect
# from tuchemnitz.forms import SubmitForm
from tuchemnitz.models import Comments

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def chemnitz(request):
    return render(request, 'stadtChemnitz.html')

def tuchemnitz(request):
    return render(request, 'tchemnitz.html')

# def map(request):
#     return render(request, 'tchemnitz.html')

def dormitory(request):
    return render(request, 'dormitory.html')

def contact(request):
    return render(request, 'contactus.html')

def news(request):
    return render(request, 'news.html')

def conversations(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comments')

        Comments.objects.create(name=name, email=email, comment=comment)
        # Here you would typically save the comment to the database
        # For example: Comments.objects.create(name=name, email=email, comment=comment)

        # return render(request, 'submit.html', {'name': name, 'email': email, 'comment': comment})
        return redirect('conversations')
    
    return render(request, 'conversations.html', {'comments': Comments.objects.all()})