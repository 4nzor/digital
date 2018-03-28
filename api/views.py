from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from first.models import Org, Platform, App


@csrf_exempt
def check_coords(request):
    if request.is_ajax():
        cord_list = []
        name_list = []
        user = Org.objects.get(username=request.user)
        lat = Platform.objects.filter(Org=user)
        coords = lat.values('lat', 'lng')
        names = lat.values('name')
        for name in names:
            name_list.append(name)
        for coord in coords:
            cord_list.append(coord)
        json_coords = {
            'data': cord_list,
            'name': name_list
        }
        return JsonResponse(json_coords)


@csrf_exempt
def get_platforms(request):
    if request.is_ajax():
        platform_list = []
        platforms = Platform.objects.filter(platform_country=request.POST['country'])
        for platform in platforms:
            platform_list.append(platform.name)

        data = {'platforms': platform_list}
        return JsonResponse(data)


@csrf_exempt
def get_apps(request):
    if request.is_ajax():
        app_list = []
        date_list = []
        if request.POST['type_command'] == 'planned':

            apps = App.objects.filter(date=request.POST['date'], is_consired=True)
            for app in apps:
                app_list.append(app.lecture_title)
                date_list.append(app.date)
        elif request.POST['type_command'] == 'completed':
            print(request.POST)
            apps = App.objects.filter(is_complete=True, date=request.POST['date'])
            print(apps)
            for app in apps:
                app_list.append(app.lecture_title)
                date_list.append(app.date)
        elif request.POST['type_command'] == 'canceled':
            apps = App.objects.filter(date=request.POST['date'], is_canceled=True)
            for app in apps:
                app_list.append(app.lecture_title)
                date_list.append(app.date)
        data = {'titles': app_list,
                'date': date_list,
                }
        print(data)
        return JsonResponse(data)
