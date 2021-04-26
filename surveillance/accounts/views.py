from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import *
from detection.models import *
from notification.views import new_user_notification_email


def new_user_notification(newusername):
	user = User.objects.get(username=newusername)
	userid = int(user.id)
	new_user_notification_email(userid)
def registerPage(request):
	if request.user.is_staff:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			notification_user = User.objects.get(username=user)
			new_user_notification_email(notification_user.id)
			# new_user_notification(user)
			messages.success(request, 'Please contact the user to check the email. Account was created for ' + user)
			return redirect('admin_page')
		context = {'form':form}
		return render(request, 'accounts/register.html', context)
	else:
		return redirect('home')


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				if request.user.is_staff:
					return redirect('admin_page')
				else:
					return redirect('user_page')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def home(request):
	context={}
	return render(request, 'accounts/dashboard.html', context)

def admin_page(request):
	context = {}
	return render(request, 'accounts/admin_page.html', context)

def user_page(request):
	context = {}
	return render(request, 'accounts/user_page.html', context)

def report_data(request):
	context = {}
	return render(request, 'accounts/report_data.html', context)

def photos(request):
	photos = Detection.objects.all()
	return render(request, 'accounts/photos.html', {'photos' : photos})

def log_report(request):
	logs = Detection.objects.all()
	return render(request, 'accounts/log_report.html', {'logs' : logs})

def user_management(request):
	context = {}
	return render(request, 'accounts/user_management.html', context)

def all_users(request):
	users = User.objects.all()
	return render(request, 'accounts/all_users.html', {'users' : users})

def delete_user(request):
	users = User.objects.all()
	return render(request, 'accounts/delete_user.html', {'users' : users})

def delete_user_confirm(request, pk_delete_user):
	user = User.objects.get(id = pk_delete_user)

	return render(request, 'accounts/delete_user_confirm.html', {'user' : user})

def delete_user_success(request, pk_delete_user_success):
	# user = User.objects.get(id = pk_delete_user)
	# context = {'user' : user}
	# context = {}

	# try:
	user = User.objects.get(id = pk_delete_user_success)
	user.delete()
	messages.success(request, 'User Deleted Successfully')
	return redirect('admin_page')
		# context['msg'] = 'The user deleted successfully'
	# except User.DoesNotExist:
	# 	context['msg'] = 'User does not exist'
	# except Exception as e:
	# 	context['msg'] = 'e.message'

	# return render(request, 'accounts/delete_user_confirm.html', context=context)

