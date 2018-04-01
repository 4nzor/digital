from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='sec_database'),
    path('search/', views.search, name='sec_search'),
    path('questionnaire/', views.questionnaire, name='sec_questionnaire'),
    path('about/', views.about, name='sec_about'),
    path('signin/', views.signin, name='sec_signin'),
    path('profile/', views.profile, name='sec_profile'),
]
