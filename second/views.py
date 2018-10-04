from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View

# Create your views here.
from second.forms import OrgForm
from second.models import Flags, Question, Organization
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
    print(results.all())
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
    return render(request, 'second/about.html')


class Signin(View):
    def get(self, request):
        return render(request, 'second/signin.html')

    def post(self, request):
        print(request.POST.get('login'))
        user = authenticate(username=request.POST['login'],
                            password=request.POST['password'])
        login(request, user)
        code = Flags.objects.get(country=request.POST['login']).code
        return render(request, 'second/profile/profile.html', {'code': code, 'name': request.POST['login']})


def profile(request):
    code = Flags.objects.get(country=request.user).code
    return render(request, 'second/profile/profile.html', {'code': code, 'name': request.user})


def get_points(request):
    if request.method == 'GET':
        snippets = Organization.objects.all()
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