from django.shortcuts import render
from django.http import HttpResponse
import folium 
import pandas as pd
from detection.models import Tower

# Create your views here.

def index(request):
    Towers = Tower.objects.all()

    fg = folium.FeatureGroup('my map')

    for tower in Towers:
        url = "/detection/tower/{}".format(tower.id)
        blank = "_blank"
        # url = 'tower' 
        fg.add_child(folium.Marker(location=[tower.latitude, tower.longitude], tooltip = tower.name, popup="<b>Name: </b>"+tower.name+ "<br><b>Location: </b>" +tower.location+ "<br><b>Latitude: </b>" +str(tower.latitude)+
        "<br><b>Longitude: </b>" +str(tower.longitude)+ "<br><b>Go to: </b><a href ={} target={}>".format(url,blank) +tower.name+ "</a>" , icon = folium.Icon(color="green")))

# checkpost loop goes here-----------------------
    fg.add_child(folium.Marker(location=[22.3958, 92.4019], tooltip = "CheckPost 1",  popup="<b>Name: </b> CheckPost1" "<br><b>Location: </b>Bandarban Zone 1" "<br><b>Latitude: </b> 22.3958"
        "<br><b>Longitude: </b> 92.4019" "</a>" , icon = folium.Icon(color="red")))

    m = folium.Map(location=[22.3958, 92.4019], 
    zoom_start =12, tiles="Stamen Terrain")


    m.add_child(fg)

    m.add_child(folium.LatLngPopup())

    m = m._repr_html_()
    context = {
        'm' : m
    }
    return render(request, 'map/index.html', context)

def map(request):
    return HttpResponse("This is the map page")