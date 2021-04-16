from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name="index"),
	path('video_feed/<str:pk_video_feed>/', views.video_feed, name="video-feed"),  
	path('index/camera1/', views.camera_1, name="camera-1"),
	# path('tower_1/', views.tower_1, name="tower-1"),
	# path('tower_2/', views.tower_2, name="tower-2"),
	# path('tower_3/', views.tower_3, name="tower-3"),
	path('tower/<str:pk_tower>/', views.tower, name="tower")
]