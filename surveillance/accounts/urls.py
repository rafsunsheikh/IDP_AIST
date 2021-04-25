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
	path('user_management', views.user_management, name = "user-management"),
	path('all_users', views.all_users, name = "all-users"),
	path('delete_user', views.delete_user, name = "delete-user"),
	path('delete_user_confirm/<str:pk_delete_user>/', views.delete_user_confirm, name = "delete-user-confirm"),
	path('delete_user_success/<str:pk_delete_user_success>/', views.delete_user_success, name = "delete-user-success"),

]