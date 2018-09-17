from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic.base import View

# Create your views here.

def index(request):
    return render(request, 'second/index.html')

def search(request):
    return render(request, 'second/search.html')

def search_results(request):
    return render(request, 'second/search_results.html')

def questionnaire(request):
    return render(request, 'second/questionnaire.html')

def about(request):
    return render(request, 'second/about.html')

class Signin(View):
    def get(self, request):
        return render(request, 'second/signin.html')

def profile(request):
    return render(request, 'second/profile/profile.html')
