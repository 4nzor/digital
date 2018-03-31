from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('check_coors/', views.check_coords, name='check_coords'),
    path('get_platform/', views.get_platforms, name='get_platform'),
    path('get_apps/', views.get_apps, name='get_apps'),
    path('check_user/', views.check_user, name='check_user'),
    path('eventmap/',views.eventmap,name='event_map'),
    path('more_platf/<id>/',views.morep,  name = 'more_platf')
]
