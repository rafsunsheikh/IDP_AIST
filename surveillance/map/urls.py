from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = "map-index"),
    path('map/', views.map, name = "map"),
]