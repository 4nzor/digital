from django.conf.urls import url
from django.contrib.auth.views import logout
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='stipot'),
    path('about/', views.about, name='about'),
    path('eventmap/', views.eventmap, name='eventmap'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners, name='partners'),
    path('signin/', views.Signin.as_view(), name='signin'),
    path('signin/congrat', views.congrat, name='congrat'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', logout, {'template_name': 'first/index.html'}, name='logout'),
    path('profile/lecturer/', views.Lecturer.as_view(), name='lecturer'),
    path('profile/organizer/', views.organizer, name='organizer'),
    path('profile/lectures/', views.lectures, name='lectures'),
    path('profile/platforms/', views.Platforms.as_view(), name='platforms'),
    path('profile/applications/', views.Applications.as_view(), name='applications'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
    path('activate/<uidb64>/<token>/',
         views.activate, name='activate'),
    path('404/', views.pagenotfound, name='pagenotfound'),
    path('app/yes/<int:app_id>/', views.yes_app, name='yes'),
]
