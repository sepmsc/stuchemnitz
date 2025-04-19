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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        # Save the comment to the database or perform any other action
        # For example, you can create a new Comment object and save it
        # comment_obj = Comments(name=name, email=email, comment=comment)
        # comment_obj.save()
        # Redirect to the same page or another page after saving
        return render(request, 'conversations.html', {'success': True})
    return render(request, 'conversations.html')