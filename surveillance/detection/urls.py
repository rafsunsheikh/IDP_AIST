from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name="index"),
	path('video_feed_1/', views.video_feed_1, name="video-feed-1"),  
	path('index/camera1/', views.camera_1, name="camera-1")
]