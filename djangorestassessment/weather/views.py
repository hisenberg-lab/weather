from django.shortcuts import render
import requests, json
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view()
def weather_data_api(request):
    """
Returns json data of weather for the given city

    """
    city = request.query_params['city']
    result = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+settings.API_KEY)
    if not result:
        response_data = {'message':'Invalid City Name'}
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    return Response(result.text) 