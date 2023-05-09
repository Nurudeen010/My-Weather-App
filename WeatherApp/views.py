from django.shortcuts import render, redirect
import json
import urllib.request
from urllib.error import HTTPError
from django.utils.datastructures import MultiValueDictKeyError
#import sweetify

def index(request):
    data = {}
    if request.method == 'POST':
        home = request.POST.get('city')
    
        try:
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' 
                                            +home+'&appid=c37b358f857bb5917b5565975f186470').read()
        except HTTPError as e:
            # sweetify.error(request, title="Error", text="Invalid city", button="OK", timer=2500)
            print('Error code: ', e.code)
            return redirect('/')
            
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
    return render(request, 'index.html', data)
