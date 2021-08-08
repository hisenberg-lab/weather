from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('weather_data/', views.weather_data_api,name='get_weather_by_city'),
]