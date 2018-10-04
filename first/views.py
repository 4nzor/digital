from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from first.models import Account, Org, Platform, App
from first.tokens import account_activation_token


def index(request):
    return render(request, 'first/index.html')


def about(request):
    return render(request, 'first/about.html')


def faq(request):
    return render(request, 'first/faq.html')


def partners(request):
    return render(request, 'first/partners.html')


class Signin(View):
    def get(self, request):
        return render(request, 'first/sign/signin.html')

    def post(self, request):
        user = request.POST['username']
        user = user.replace(" ", "")
        password = request.POST['pass']
        user = authenticate(username=user, password=password)

        try:
            login(request, user)
            Org.objects.get(username=user)
            return redirect('/stipot/profile/organizer/')
        except Org.DoesNotExist:
            return redirect('/stipot/profile/lecturer/')
        except AttributeError:
            return render(request, 'first/sign/signin.html', {'error_login': "1", 'username_error': user})


def congrat(request):
    return render(request, 'first/sign/congrat.html')


class Register(View):
    def get(self, request):
        return render(request, 'first/sign/register.html')

    def post(self, request):
        type_reg = request.POST.get('reg_whoiam')
        if type_reg == 'lecture':
            try:
                Account.objects.create_user(
                    username=request.POST['username'],
                    full_name=request.POST['full_name'],
                    email=request.POST['email'],
                    password=request.POST['pass'],
                    is_active=False
                )
            except IntegrityError:
                return render(request, 'first/404.html')
            user = Account.objects.get(username=request.POST['username'])
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
            return render(request, 'first/sign/register.html', {'success': 'success'})

        elif type_reg == 'org':
            Org.objects.create_user(
                username=request.POST['username'],
                full_name=request.POST['full_name'],
                email=request.POST['email'],
                password=request.POST['pass'],
                is_active=False
            )
            user = Org.objects.get(username=request.POST['username'])
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
            return render(request, 'first/sign/register.html', {'success': 'success'})


def eventmap(request):
    return render(request, 'first/eventmap.html',
                  {'platform': Platform.objects.all(), 'lecture': App.objects.filter(is_consired=True)}
                  )


class Lecturer(View):
    def get(self, request):
        try:
            acc = Account.objects.get(username=request.user)
            return render(request, 'first/users/lecturer.html', {'acc': acc})
        except:
            return render(request, 'first/404.html')

    @login_required
    @csrf_exempt
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
        try:
            user.female = request.POST['lect_mrs_lect']
        except:
            pass
        user.position = request.POST['position']
        user.save()
        return redirect('/stipot/profile/lecturer/')


class Organizer(View):
    def get(self, request):
        try:
            return render(request, 'first/users/organizer.html', {'org': Org.objects.get(username=request.user)})
        except:
            return render(request, 'first/404')

    @csrf_exempt
    def post(self, request):
        org = Org.objects.get(username=request.user)
        org.lecture_themes = request.POST['thems']
        org.full_name = request.POST['name']
        org.director = request.POST['director']
        org.director_email = request.POST['email_dir']
        org.email = request.POST['email']
        org.country = request.POST['countries']
        org.phone_number = request.POST['number']
        org.resperative = request.POST['rep']
        org.save()
        print('cdsc')
        return redirect('.')


def lectures(request):
    try:
        Account.objects.get(username=request.user)
        return render(request, 'first/users/lectures.html', {'lect': Account.objects.get(username=request.user)})
    except:
        return render(request, 'first/404.html')


class Platforms(View):
    def get(self, request):
        try:
            Org.objects.get(username=request.user)
            return render(request, 'first/users/platforms.html')
        except:
            return render(request, 'first/404.html')

    @csrf_exempt
    def post(self, request):
        Platform.objects.create(
            name=request.POST['name'],
            platform_city=request.POST['city'],
            platform_country=request.POST['country'],
            platform_adress=request.POST['adress'],
            lat=request.POST['lat'],
            lng=request.POST['lng'],
            Org=Org.objects.get(username=request.user)
        )
        return redirect('.')


class Applications(View):
    def get(self, request):
        try:
            Account.objects.get(username=request.user)
            return render(request, 'first/users/applications.html', {
                'cons_app': App.objects.filter(is_consired=False),
                'platform': Platform.objects.all(),
                'apps': App.objects.filter(user__username=request.user)
            })
        except:
            return render(request, 'first/404.html')

    @csrf_exempt
    def post(self, request):
        current_site = get_current_site(request)
        App.objects.create(
            user=Account.objects.get(username=request.user),
            country=request.POST['country'],
            platform=Platform.objects.get(name=request.POST['platform']),
            date=request.POST['date'],
            lecture_title=request.POST['title_app'],
            language=request.POST['language'],
            is_consired=False
        )

        app_email = Account.objects.get(username=request.user).email
        platform_email = Platform.objects.get(name=request.POST['platform']).Org
        subject, from_email, to = 'Application from STIPOT', app_email, platform_email.email
        html_content = render_to_string('first/app_confir.html',
                                        {'username': Account.objects.get(username=request.user),
                                         'date': request.POST['date'],
                                         'title': request.POST['title_app'], 'platform': request.POST['platform'],
                                         'domain': current_site.domain,
                                         'id': App.objects.get(lecture_title=request.POST['title_app']).id})

        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [platform_email.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect('.')


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
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        return render(request, 'first/sign/congrat.html', {'succes': 'success'})
    else:
        return render(request, 'first/404.html')


def pagenotfound(request):
    return render(request, 'first/404.html')


def yes_app(request, app_id):
    app = App.objects.get(id=app_id)
    app.is_consired = True
    app.save()
    return render(request, 'first/index.html')


@csrf_exempt
def upload_avatar_org(request):
    user = Org.objects.get(username=request.user)
    msg = 'notNone'
    try:
        user.logo.url
    except:
        msg = 'None'

    user.logo.delete()
    user.logo = request.FILES['photo']
    user.save()
    return JsonResponse({'url': user.logo.url, 'msg': msg})


def delete_avatar(request):
    user = Account.objects.get(username=request.user)
    user.avatar.delete()
    user.save()
    return JsonResponse({"massage": "okey"})


def delete_avatar_org(request):
    user = Org.objects.get(username=request.user)
    user.logo.delete()
    user.save()
    return JsonResponse({"massage": "okey"})


def all_lecturers(request):
    return render(request, 'first/users/all_lecturers.html')


def logout_view(request):
    logout(request)
    return redirect('/')