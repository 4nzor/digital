from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

from first.models import Account, Org
from first.tokens import account_activation_token


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
        return render(request, 'first/sign/signin.html')

    def post(self, request):
        user = request.POST['username']
        user = user.replace(" ", "")
        password = request.POST['pass']
        user = authenticate(username=user, password=password)

        login(request, user)
        try:
            Org.objects.get(username=user)
            return redirect('/profile/organizer/')
        except Org.DoesNotExist:
            return redirect('/profile/lecturer/')


def congrat(request):
    return render(request, 'first/sign/congrat.html')

class register(View):
    def get(self, request):
        return render(request, 'first/sign/register.html')

    def post(self, request):
        type_reg = request.POST.get('reg_whoiam')
        if type_reg == 'lecture':
            Account.objects.create_user(
                username=request.POST['username'],
                full_name=request.POST['full_name'],
                email=request.POST['email'],
                password=request.POST['pass'],
                is_active=False
            )
            user = User.objects.get(username=request.POST['username'])
            current_site = get_current_site(request)

            mail_subject = 'STIPOT:Activate your account.'
            domain = current_site.domain
            uid = user.id
            token = account_activation_token.make_token(user)
            message = render_to_string('first/sign/acc_active_email.html',
                                       {
                                           'user': user,
                                           'domain': domain,
                                           'token': token,
                                           'uid': uid,

                                       })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, from_email='zokgb05@gmaail.com', to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

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

class lecturer(View):
    def get(self, request):
        acc = Account.objects.get(username=request.user)

        return render(request, 'first/users/lecturer.html', {'acc': acc})

    def post(self, request):
        user = Account.objects.get(username=request.user)
        user.full_name = request.POST['name']
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

def lectures(request):
    return render(request, 'first/users/lectures.html')

def applications(request):
    return render(request, 'first/users/applications.html')

@csrf_exempt
def upload_avatar(request):
    user = Account.objects.get(username=request.user)
    msg = 'notNone'
    try:
        user.avatar.url
    except:
        msg = 'None'

    user.avatar.delete()
    user.avatar = request.FILES['photo']
    user.save()
    return JsonResponse({'url': user.avatar.url, 'msg': msg})


def activate(request, uidb64, token):
    try:

        user = User.objects.get(id=uidb64)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        print(12)
    if user is not None and account_activation_token.check_token(user, token):
        print(3)
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
