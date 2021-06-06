from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http.response import StreamingHttpResponse
from django.core.files.base import ContentFile
from .models import Detection
from notification import views as notification_views
from time import time
from .models import Tower


from imutils.video import VideoStream
from imutils.video import FPS
from PIL import Image
from io import BytesIO
import numpy as np
import argparse
import imutils
import time
import cv2
from threading import *
from time import sleep


# proto_file = r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance\detection\MobileNetSSD_deploy.prototxt.txt'
# caffe_model = r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance\detection\MobileNetSSD_deploy.caffemodel'
proto_file = r'static/MobileNetSSD_deploy.prototxt.txt'
caffe_model = r'static/MobileNetSSD_deploy.caffemodel'
start_time = 0

#Home Page ---------------------------------
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))
# ----------------------------------
#Tower List Page ---------------------------------
def tower_list(request):

    towers = Tower.objects.all()
    return render(request, "tower_list.html", {'towers': towers})
    # template = loader.get_template('tower_list.html')
    # return HttpResponse(template.render({}, request))

# ----------------------------------

#Tower 1 ---------------------------------
def tower(request,pk_tower):
    tower = Tower.objects.get(id=pk_tower)
    context = {'tower':tower}
    # template = loader.get_template('tower.html')
    return render(request,'tower.html',context)
# ----------------------------------

# Camera 1 ----------------------------
def camera_1(request):
    template = loader.get_template('camera1.html')
    return HttpResponse(template.render({}, request))
# ------------------------------------

# Display camera 1 ------------------------
def stream(camera_select):
    global start_time
    start_time = time.time()
    # file = open(r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance\detection\number.txt', 'r')
    file = open(r'static/number.txt', 'r')
    number = int(file.read())
    file.close()
    # initialize the list of class labels MobileNet SSD was trained to
    # detect, then generate a set of bounding box colors for each class
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	    "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	    "sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

    # load our serialized model from disk
    print("[INFO] loading model...")
    net = cv2.dnn.readNetFromCaffe(proto_file, caffe_model)

    # initialize the video stream, allow the cammera sensor to warmup,
    # and initialize the FPS counter
    # cam_id = 0
    # vid = cv2.VideoCapture(cam_id)
    print("[INFO] starting video stream...")
    vs = VideoStream(src = int(camera_select)-1).start()
    # vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)
    fps = FPS().start()

    # loop over the frames from the video stream
    while True:
        # grab the frame from the threaded video stream and resize it
        # to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=900)

        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
            0.007843, (300, 300), 127.5)

        # pass the blob through the network and obtain the detections and
        # predictions
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > 0.2:
                # extract the index of the class label from the
                # `detections`, then compute the (x, y)-coordinates of
                # the bounding box for the object

                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # draw the prediction on the frame
                label = "{}: {:.2f}%".format(CLASSES[idx],
                   confidence * 100)
                print("[INFO] {}".format(label))

                cv2.rectangle(frame, (startX, startY), (endX, endY),
                    COLORS[idx], 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

                label_to_generate_alarm = CLASSES[idx]
                if label_to_generate_alarm == "person":
                    print("Generate Alarm")
                    t1 = Generate_alarm()
                    t1.start()
                    ret, buf = cv2.imencode('.jpg', frame)
                    content = ContentFile(buf.tobytes())

                    # Saving detection logs to model Detection
                    result = Detection()
                    result.name = 'human{}.jpg'.format(number)
                    result.image.save('output{}.jpg'.format(number), content)
                    result.save()
                    notification(result, number)

                    # Setting image number for next detection
                    # file2 = open(r'C:\Users\MD Rafsun Sheikh\Desktop\IDP_AIST\surveillance\detection\number.txt', 'w')
                    file2 = open(r'static/number.txt', 'w')
                    file2.write(str(number))
                    file2.close()
                    
                    # im_pil = Image.fromarray(frame)
                    # buffer = BytesIO()
                    # im_pil.save(buffer, format='png')
                    # image_png = buffer.getvalue()
                    # result = cv2.imwrite(r'persons\human{}.png'.format(number), frame)
                    # result = Detection.objects.create(name = 'human{}.jpg'.format(number), image = image_png)
                    # result.save()
                    number += 1
            
        imgencode = cv2.imencode('.jpg', frame)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')

      
        # show the output frame
    #     cv2.imshow("Frame", frame)
    #     key = cv2.waitKey(1) & 0xFF
        # cv2.imwrite("Frame", frame)
        

        # yield(b'--frame1\r\n'
                        # b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')

    #     # if the `q` key was pressed, break from the loop
    #     if key == ord("q"):
    #         break

        # update the FPS counter
        # fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # # do a bit of cleanup

    cv2.destroyAllWindows()
    vs.stop()


def video_feed(request, pk_video_feed):
    camera_select = pk_video_feed
    return StreamingHttpResponse(stream(camera_select), content_type = 'multipart/x-mixed-replace; boundary = frame')
# ------------------------------------------------------

def notification(result, number):
    global start_time
    detection_time_elapsed = False
    compare_time = time.time()
    if compare_time - start_time > 300:
        notification_views.detection_email_incl_attachment(result, number)
        start_time = compare_time

class Generate_alarm(Thread):
    def run(self):
        from playsound import playsound
        path = r'static/alarms/5.mp3'
        playsound(path)   
        sleep(60)  

