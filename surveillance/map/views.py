from django.shortcuts import render
from django.http import HttpResponse
import folium 
import pandas as pd

# Create your views here.

def index(request):
    data = pd.read_csv(r"C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance\static\tower_location.csv", encoding = "cp1252")

    latitudes = list(data['Latitude'])
    longitudes = list(data['Longitude'])
    names = list(data['Name'])
    locations = list(data['Location'])
    links = list(data['Link'])

    fg = folium.FeatureGroup('my map')

    for latitude, longitude, name, location, link in zip(latitudes, longitudes, names, locations, links):
        fg.add_child(folium.Marker(location=[latitude, longitude], tooltip = name, popup="<b>Name: </b>"+name+ "<br><b>Location: </b>" +location+ "<br><b>Latitude: </b>" +str(latitude)+
        "<br><b>Longitude: </b>" +str(longitude)+ "<br><b>Go to: </b><a href = "+link+">" +name+ "</a>" , icon = folium.Icon(color="green")))

    m = folium.Map(location=[22.1823184841715, 92.384033203125], 
    zoom_start =12, tiles="Stamen Terrain")

    # tooltip = "Tower 1"

    # folium.Marker([22.30688482518366, 92.54058837890625], 
    # tooltip=tooltip, popup = "country",
    # icon = folium.Icon(color = "red", icon = "cloud"),
    # ).add_to(m)
    m.add_child(fg)

    m.add_child(folium.LatLngPopup())

    m = m._repr_html_()
    context = {
        'm' : m
    }
    return render(request, 'map/index.html', context)

def map(request):
    return HttpResponse("This is the map page")