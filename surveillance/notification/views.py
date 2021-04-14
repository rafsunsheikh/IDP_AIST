from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    receivers = []
    for user in users:
        receivers.append(user.email)
    send_mail(
        'Hello from AIST',
        'Hello, this is auto generated email. Please give feedback on the email',
        settings.EMAIL_HOST_USER,
        receivers,
        fail_silently=False
    )
    return render(request, 'notification/index.html')

def detection_notification():
    User = get_user_model()
    users = User.objects.all()
    receivers = []
    for user in users:
        receivers.append(user.email)
    send_mail(
        'Detection Alert',
        'Assalamu alaikum sir,\nTrespassing is detected at the area of tower 1.\nPlease login system to verify.\nNotification from AIST',
        settings.EMAIL_HOST_USER,
        receivers,
        fail_silently=False
    )