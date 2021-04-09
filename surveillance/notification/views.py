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
