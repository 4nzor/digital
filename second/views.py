from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'second/index.html')

def search(request):
    return render(request, 'second/search.html')

def questionnaire(request):
    return render(request, 'second/questionnaire.html')

def about(request):
    return render(request, 'second/about.html')

def signin(request):
    return render(request, 'second/signin.html')

def profile(request):
    return render(request, 'second/profile/profile.html')