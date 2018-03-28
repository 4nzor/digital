from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('second/', views.index, name='database'),
    path('second/search', views.search, name='search'),
    path('second/questionnaire', views.questionnaire, name='questionnaire'),
    path('second/about', views.about, name='about'),
    path('second/signin', views.signin, name='signin'),

    path('second/profile', views.profile, name='profile'),
]
