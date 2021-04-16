from django.urls import path
from . import views
from detection import views as detection_views
from map import views as map_views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
	path('admin_page', views.admin_page, name = "admin_page"),
	path('user_page', views.user_page, name = "user_page"),
	path('tower_feed', detection_views.index, name= "tower-feed"),
	path('tower_list', detection_views.tower_list, name= "tower-list"),
	path('report_data', views.report_data, name = "report-data"),
	path('photos', views.photos, name = "photos"),
	path('log_report', views.log_report, name = 'log-report'),
	path('sitemap', map_views.index, name = 'map'),

]