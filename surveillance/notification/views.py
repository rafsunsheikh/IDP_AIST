from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
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
    fromaddr = "rafsunsheikh116@gmail.com"
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
    server.login(fromaddr, "barisalcadetcollege1630")
    server.sendmail(fromaddr, receivers, text)
    server.quit()