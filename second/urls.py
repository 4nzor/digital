from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('second/', views.index, name='sec_database'),
    path('second/search', views.search, name='sec_search'),
    path('second/questionnaire', views.questionnaire, name='sec_questionnaire'),
    path('second/about', views.about, name='sec_about'),
    path('second/signin', views.signin, name='sec_signin'),

    path('second/profile', views.profile, name='sec_profile'),
]
