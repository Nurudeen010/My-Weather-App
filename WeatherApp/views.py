from django.shortcuts import render
import json
import urllib.request
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city.is_valid():
            try:
                source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' 
                                            +city+'&units=metric&appid=c37b358f857bb5917b5565975f186470').read()
                our_data = json.loads(source)
                data = {
                "country_code": str(our_data['sys']['country']),
                "coordinate": str(our_data['coord']['lon']) + ', '
                + str(our_data['coord']['lat']),

                "temp": str(our_data['main']['temp']) + ' °C',
                "pressure": str(our_data['main']['pressure']),
                "humidity": str(our_data['main']['humidity']),
                'main': str(our_data['weather'][0]['main']),
                'description': str(our_data['weather'][0]['description']),
                'icon': our_data['weather'][0]['icon'],
                }

                print (data)
            except:
                print("An error occurred")
    else:
        data = {}
    return render(request, 'index.html', data)
