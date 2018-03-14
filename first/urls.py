from django.contrib.auth.views import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='stipot'),
    path('about/', views.about, name='about'),
    path('eventmap/', views.eventmap, name='eventmap'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners, name='partners'),
    path('signin/', views.signin.as_view(), name='signin'),
    path('register/', views.register.as_view(), name='register'),
    path('logout/', logout, {'template_name': 'first/index.html'}),
    path('account/', views.profile, name='profile'),
    path('profile/lecturer/', views.lecturer, name='lecturer'),
    path('profile/organizer/', views.organizer, name='organizer')
]
