from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('check_coors/', views.check_coords, name='check_coords'),
    path('get_platform/', views.get_platforms, name='get_platform'),
    path('get_apps/', views.get_apps, name='get_apps')

]
