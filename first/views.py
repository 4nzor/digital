from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from django.views.generic.base import View

from first.models import Account, Org


def index(request):
    return render(request, 'first/index.html')


def about(request):
    return render(request, 'first/about.html')


def faq(request):
    return render(request, 'first/faq.html')


def partners(request):
    return render(request, 'first/partners.html')


class signin(View):
    def get(self, request):
        return render(request, 'first/signin.html')

    def post(self, request):
        user = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=user, password=password)

        login(request, user)
        try:
            Org.objects.get(username=user)
            return redirect('/profile/organizer/')
        except Org.DoesNotExist:
            return redirect('/profile/lecturer/')


class register(View):
    def get(self, request):
        return render(request, 'first/register.html')

    def post(self, request):
        type_reg = request.POST.get('reg_whoiam')
        if type_reg == 'lecture':
            Account.objects.create_user(
                username=request.POST['username'],
                full_name=request.POST['full_name'],
                email=request.POST['email'],
                password=request.POST['pass'],
            )
            return redirect('/signin')
        else:
            Org.objects.create_user(
                username=request.POST['username'],
                full_name=request.POST['full_name'],
                email=request.POST['email'],
                password=request.POST['pass'],
            )
            return redirect('/signin')


def eventmap(request):
    return render(request, 'first/eventmap.html')


def profile(request):
    return render(request, 'first/account.html')


class lecturer(View):
    def get(self, request):
        acc = Account.objects.get(username=request.user)
        return render(request, 'first/users/lecturer.html', {'acc': acc})

    def post(self, request):
        user = Account.objects.get(username=request.user)
        user.username = request.POST['name']
        user.placeOfWork = request.POST['place']
        user.country = request.POST['countries']
        user.science_degree = request.POST['degree']
        user.orc_id = request.POST['orc_id']
        user.researcher_id = request.POST['res_id']
        user.scientific_interest = request.POST['interests']
        user.academic_rank = request.POST['rank']
        user.sex = request.POST['lect_sex_lect']
        user.position = request.POST['position']
        user.save()
        return redirect('/profile/lecturer/')


def organizer(request):
    return render(request, 'first/users/organizer.html')
