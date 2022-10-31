import requests
import cv2
import json
import pprint
import numpy as np

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width, height)

while True:
    ret, frame = cap.read()

    # #Convert frame to jpg
    # ret, jpg = cv2.imencode('.jpg', frame)

    #convert frame to bytes
    jpg = cv2.imencode('.jpg', frame)[1].tobytes()

    # frame = cv2.imread('bus.jpg')
    DETECTION_URL = "http://192.168.1.7:5000/v1/object-detection/yolov5x6"
    # IMAGE = "bus.jpg"
    # with open(IMAGE, "rb") as f:
    #     image_data = f.read()
        
    response = requests.post(DETECTION_URL, files={"image": jpg}).json()

    for obj in response:
        frame = cv2.rectangle(frame, (int(obj['xmin']), int(obj['ymin'])), (int(obj['xmax']), int(obj['ymax'])), (0, 255, 0), 2)
        frame = cv2.putText(frame, obj['name'], (int(obj['xmin']), int(obj['ymin']) - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2, cv2.LINE_AA, False)


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break