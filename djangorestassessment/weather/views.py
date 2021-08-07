from django.shortcuts import render
import requests, json
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view()
def weather_data_api(request):
    """
Makes an API call to the open source weather API
Gets the response in json format
Returns the same json data received above and send it to the API caller

    """
    city = request.query_params['city']
    result = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dfd763dcff52ad64fddb4e8b8a5502f0")
    if not result:
        response_data = {'message':'Invalid City Name'}
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    return Response(result.text) 