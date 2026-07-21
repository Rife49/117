from django.shortcuts import render

# Create your views here.
def about_me (request):
    return render(request, 'pages/about_me.html')

def experience (request):
    return render(request, 'pages/experience.html')

def contact(request):
    return render(request, 'pages/contact.html')