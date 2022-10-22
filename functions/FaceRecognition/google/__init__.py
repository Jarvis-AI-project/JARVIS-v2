#https://youtu.be/sz25xxF_AVE
#----------------1. find faces (HOG)------------------
# https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78

#pip install cmake, dlib, wheel, face_recognition, numpy, opencv-python

import cv2
import face_recognition as fr
import numpy as np

#loading main image
image = fr.load_image_file('img/train/image_dhruv_01.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#finding face in main image
face_locations = fr.face_locations(image)[0]  # eg-(204, 461, 590, 76)
cv2.rectangle(image, (face_locations[3], face_locations[0]), (face_locations[1], face_locations[2]), (255, 0, 255), 2)
#encoding face in main image
encoded_image = fr.face_encodings(image)[0]

#loading test image
test_image = fr.load_image_file('img/test/image_dhruv_test_03.jpg')
test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
# cv2.imshow('test_image', test_image)
# cv2.waitKey(0)
#finding face in test image
face_locations_test = fr.face_locations(test_image)[0]
print(face_locations_test)
cv2.rectangle(test_image, (face_locations_test[3], face_locations_test[0]), (face_locations_test[1], face_locations_test[2]), (255, 0, 255), 2)
#encoding face in test image
encoded_test_image = fr.face_encodings(test_image)[0]

#comparing faces
results = fr.compare_faces([encoded_image], encoded_test_image)
print(results)



cv2.imshow('Dhruv', image)
cv2.imshow('Dhruv Test', test_image)
cv2.waitKey(0)