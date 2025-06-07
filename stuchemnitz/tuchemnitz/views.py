from django.shortcuts import render, redirect
from tuchemnitz.forms import AdminSignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
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

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            login(request, user)
            return redirect('admin_profile')  # Redirect to a success page or similar
    else:
        form = AdminSignupForm()

    return render(request, 'admin_signup.html', {'form': form})  # Render the signup form

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_profile(request):
    return render(request, 'admin_profile.html', {'user': request.user})  # Render the admin profile page