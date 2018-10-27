from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View

# Create your views here.
from second.forms import OrgForm
from second.models import Flags, Question, Organization, About
from second.serializers import SnippetSerializer


def index(request):
    return render(request, 'second/index.html')


def search(request):
    return render(request, 'second/search.html')


def search_results(request):
    results = Organization.objects.filter(Q(country__icontains=request.GET['country']),
                                          Q(org_name__icontains=request.GET['org_name']),
                                          Q(location__icontains=request.GET['location']),
                                          Q(contact_person__icontains=request.GET['contact_person']),
                                          Q(sci_area__icontains=request.GET['sci_area']),
                                          Q(activities__icontains=request.GET['activities']),
                                          Q(conditions_on_access__icontains=request.GET['conditions_on_access']),
                                          )
    return render(request, 'second/search_results.html', {'results': results})


class Questionnaire(View):
    def get(self, request):
        return render(request, 'second/questionnaire.html', {'questions': Question.objects.filter(status=True)})

    def post(self, request):
        Organization.objects.create(country=request.POST.get('country'),
                                    owner_name=request.POST.get('owner_name'),
                                    org_name=request.POST.get('org_name'),
                                    location=request.POST.get('location'),
                                    site=request.POST.get('site'),
                                    contact_person=request.POST.get('contact_person'),
                                    email=request.POST.get('email'),
                                    inst_type=request.POST.get('inst_type'),
                                    short_description_org=request.POST.get('short_description_org'),
                                    short_description_infr=request.POST.get('short_description_infr'),
                                    sci_area=request.POST.get('sci_area'),
                                    activities=request.POST.get('activities'),
                                    conditions_on_access=request.POST.get('conditions_on_access'),
                                    restrictions=request.POST.get('restrictions'),
                                    inter_cooperation=request.POST.get('inter_cooperation'),
                                    # lat=request.POST.get('lat'),
                                    # lon=request.POST.get('lon')
                                    )
        return render(request, 'second/questionnaire.html', {'questions': Question.objects.filter(status=True)})


def about(request):
    return render(request, 'second/about.html', {'abouts': About.objects.all()})


class Signin(View):
    def get(self, request):
        return render(request, 'second/signin.html')

    def post(self, request):
        try:
            user = authenticate(username=request.POST['login'],
                                password=request.POST['password'])
            login(request, user)
            if request.user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('/database/profile')
        except:
            return render(request, 'second/signin.html', {'error': 'error'})


@login_required
def profile(request):
    if request.user.is_superuser:
        return redirect('/admin')
    else:
        try:
            code = Flags.objects.get(country=request.user).code
            applications = Organization.objects.filter(country=request.user, hided=False)
            return render(request, 'second/profile/profile.html',
                          {'code': code, 'name': request.user, 'apps': applications})
        except Flags.DoesNotExist:
            logout(request)
            return render(request, 'second/signin.html', {'error': 'error'})


def get_points(request):
    if request.method == 'GET':
        snippets = Organization.objects.filter(is_confirm=True)
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


def hide_input(request):
    inpt = request.POST.get('name')
    question_edit_status = Question.objects.get(name=inpt)
    question_edit_status.status = False
    question_edit_status.save()
    return HttpResponse('ok')


def logout_view(request):
    logout(request)
    return redirect('/database')


def control(request):
    command = request.POST['command']
    id = request.POST['id']
    org = Organization.objects.get(id=id)
    if command == 'complete':
        org.is_confirm = True
        org.hided = True
        org.save()
    if command == 'hide':
        org.hided = True
        org.save()

    if command == 'reject':
        org.is_confirm = False
        org.hided = True
        org.save()
    return JsonResponse({'Status': 200})


def show_details(request, id):
    org = get_object_or_404(Organization, id=id)
    return render(request, 'second/show_details.html',{'org' : org})
