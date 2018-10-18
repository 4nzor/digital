from django.conf.urls import url
from django.urls import path, re_path
from second import views
from second import generate_data

urlpatterns = [
    path('', views.index, name='sec_database'),
    path('search/', views.search, name='sec_search'),
    path('results/', views.search_results, name='sec_search_results'),
    path('questionnaire/', views.Questionnaire.as_view(), name='sec_questionnaire'),
    path('about/', views.about, name='sec_about'),
    path('signin/', views.Signin.as_view(), name='sec_signin'),
    path('profile/', views.profile, name='sec_profile'),
    path('get_points/', views.get_points, name='get_points'),
    path('gendata/', generate_data.generate_fake_data),
    path('hide_input/',views.hide_input),
    path('logout/',views.logout_view , name='logout'),
]
