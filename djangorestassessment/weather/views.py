from django.shortcuts import render
import requests, json
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get("city")
        result = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+settings.API_KEY)
        if result:
            api_data = json.loads(result.text)
            data = {"city": str(api_data["name"]),
                    "coordinates": "Lon "+str(api_data["coord"]["lon"])+" "+"Lat "+str(api_data["coord"]["lat"]),
                    "weather": str(api_data["weather"][0]["description"]),
                    "temp": "temp "+str(api_data["main"]["temp"])+", "+"feels like "+str(api_data["main"]["feels_like"]),
                    "humidity": str(api_data["main"]["humidity"]),
                    }
            # print(data)
        else:
            data={"error":1}
        return render(request,"index.html",data)
    return render(request,"index.html")

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
    return Response(result.json()) 