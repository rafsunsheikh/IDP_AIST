from django.urls import path
from . import views
from detection import views as detection_views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
	path('admin_page', views.admin_page, name = "admin_page"),
	path('user_page', views.user_page, name = "user_page"),
	path('tower_feed', detection_views.index, name= "tower-feed")
]