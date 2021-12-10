from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from detection.models import Detection
from datetime import datetime


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

def detection_email_incl_attachment(result, number):
    fromaddr = "youremail"
    User = get_user_model()
    users = User.objects.all()
    receivers = []
    for user in users:
        receivers.append(user.email)

    msg = MIMEMultipart()
    msg['From'] = "AIST <{}>".format(fromaddr)
    msg['To'] = ','.join(receivers)
    msg['Subject'] = "Detection Alert"

    date = result.detection_date.strftime("%m/%d/%Y")
    time = result.detection_time.strftime("%H:%M:%S")
    
    # body = "Assalamu alaikum sir,\nTrespassing is detected at the area of tower 1.\nPlease login system to verify.\n\nNotification from AIST"
    msg.attach(MIMEText('<html><body>' + "<h2>AI Surveillance Tower</h2><hr>" + "<br><br>" +
    "Assalamu alaikum sir," + "<br>" + 
    "Tresspassing is detected at the area of tower 1." + "<br>" + 
    "Please login system to verify." + "<br><br>" + 
    "<h3>Detection Info:</h3>" + "<strong>Detection Name: </strong>" + result.name + 
    "<br><strong>Detection Date: </strong>" + date +
    "<br><strong>Detection time: </strong>" + time +
    "<br><br> This is an automatic generated email.Please don't reply to the email" + 
    "<br><br><strong>Notification from AIST. An AI based surveillance system.</strong>" +
    "</html></body>", 'html', 'utf-8'))
    # msg.attach(MIMEText(body, 'plain'))

    # filename = r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance' + result.image.url
    filename = r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance' + result.image.url
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename = " +filename)
   
   
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "yourpass")
    server.sendmail(fromaddr, receivers, text)
    server.quit()


def new_user_notification_email(pk_new_user_id):
    fromaddr = "youremail"
    User = get_user_model()
    user = User.objects.get(id = pk_new_user_id)
    # user = User.objects.get()
    receiver = []
    receiver.append(user.email)
    # for user in users:
    #     receivers.append(user.email)

    msg = MIMEMultipart()
    msg['From'] = "AIST <{}>".format(fromaddr)
    msg['To'] = ','.join(receiver)
    msg['Subject'] = "New User Notification"

    # date = result.detection_date.strftime("%m/%d/%Y")
    # time = result.detection_time.strftime("%H:%M:%S")
    date = user.date_joined.strftime("%m/%d/%Y")
    time = user.date_joined.strftime("%H:%M:%S")
    
    # body = "Assalamu alaikum sir,\nTrespassing is detected at the area of tower 1.\nPlease login system to verify.\n\nNotification from AIST"
    msg.attach(MIMEText('<html><body>' + "<h2>AI Surveillance Tower</h2><hr>" + "<br><br>" +
    "Assalamu alaikum sir," + "<br>" + 
    "A new user is created." + "<br>" + 
    "<h2>User Details:</h2>" + "<br>" + 
    "<h3>User Info:</h3>" + "<strong>Username: </strong>" + user.username + 
    "<br><strong>User Email: </strong>" + user.email +
    "<br><strong>User Name: </strong>" + user.first_name + " " + user.last_name +
    "<br><strong>User Create Date: </strong>" + date +
    "<br><strong>User Create time: </strong>" + time +
    "<br><br> Please Contact the AIST HQ for the password.Thank you." +
    
    "<br><br><br> This is an automatic generated email.Please don't reply to the email" + 
    "<br><strong>Notification from AIST. An AI based surveillance system.</strong>" +
    "</html></body>", 'html', 'utf-8'))
    # msg.attach(MIMEText(body, 'plain'))

    # filename = r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance' + result.image.url
    # attachment = open(filename, "rb")

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename = " +filename)
    #send notifications
   
    # msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "yourpass")
    server.sendmail(fromaddr, receiver, text)
    server.quit()
