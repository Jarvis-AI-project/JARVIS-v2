# video_stream.set(cv2.CAP_PROP_FRAME_WIDTH, 2000) # set frame width
# video_stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)# set frame height

#get possible frame size
# width = video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# height = video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
# print("Frame size: " + str(width) + " x " + str(height))


import cv2
import time
from compreface import CompreFace
from compreface.service import RecognitionService

#VideoStream
video_stream = cv2.VideoCapture(0)  # 0 for webcam
video_stream.set(cv2.CAP_PROP_BUFFERSIZE, 2)    # set buffer size to 2

CompreFace = CompreFace('http://localhost', '8000', {
    # maximum number of faces on the image to be recognized. It recognizes the biggest faces first. Value of 0 represents no limit.
    "limit": 0,
    # minimum required confidence that a recognized face is actually a face
    "det_prob_threshold": 0.8,
    # maximum number of subject predictions per face. It returns the most similar subjects.
    "prediction_count": 1,
    # https://github.com/exadel-inc/CompreFace/blob/master/docs/Face-services-and-plugins.md#face-plugins
    # "face_plugins": "age,gender",
    "status": True
})
CompreFace.init_face_recognition('85b979c0-5b59-4112-a798-8092053041ca')
FPS = 1/30

while video_stream.isOpened():
    (status, frame_raw) = video_stream.read()  # read frame from video stream
    frame = cv2.flip(frame_raw, 1)  # flip frame
    cv2.imshow('JARVIS FaceID', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#release
# After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

[{'box': {'probability': 0.99744, 'x_max': 330, 'y_max': 401, 'x_min': 0, 'y_min': 13}, 'subjects': [
    {'subject': 'Devasheesh', 'similarity': 0.99928}], 'execution_time': {'detector': 2119.0, 'calculator': 274.0}}]


'''Example Result:

[
    {
        'box': {'probability': 0.9961, 'x_max': 202, 'y_max': 397, 'x_min': 0, 'y_min': 175}, 
        'subjects': [{'subject': 'Devasheesh', 'similarity': 0.99538}], 
        'execution_time': {'detector': 99.0, 'calculator': 63.0}
    }, 
    {
        'box': {'probability': 0.97642, 'x_max': 307, 'y_max': 293, 'x_min': 248, 'y_min': 233}, 'subjects': [{'subject': 'Dhruv', 'similarity': 0.55461}], 'execution_time': {'detector': 99.0, 'calculator': 63.0}}, {'box': {'probability': 0.96169, 'x_max': 547, 'y_max': 191, 'x_min': 471, 'y_min': 116}, 'subjects': [{'subject': 'Dhruv', 'similarity': 0.91141}], 'execution_time': {'detector': 99.0, 'calculator': 64.0}}, {'box': {'probability': 0.94194, 'x_max': 442, 'y_max': 199, 'x_min': 377, 'y_min': 135}, 'subjects': [{'subject': 'Dhruv', 'similarity': 0.67939}], 'execution_time': {'detector': 99.0, 'calculator': 61.0}}, {'box': {'probability': 0.8431, 'x_max': 521, 'y_max': 313, 'x_min': 459, 'y_min': 248}, 'subjects': [{'subject': 'Devasheesh', 'similarity': 0.54301}], 'execution_time': {'detector': 99.0, 'calculator': 68.0}}]
[{'box': {'probability': 0.99997, 'x_max': 357, 'y_max': 342, 'x_min': 186, 'y_min': 162}, 'subjects': [{'subject': 'Devasheesh', 'similarity': 0.98644}], 'execution_time': {'detector': 438.0, 'calculator': 104.0}}]

'''
