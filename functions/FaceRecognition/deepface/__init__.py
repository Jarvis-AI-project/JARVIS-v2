from deepface import DeepFace
import datetime
# Read more at: https://viso.ai/computer-vision/deepface/
# https://viso.ai/computer-vision/deepface/
start = datetime.datetime.now()
verification = DeepFace.verify(
    img1_path="img\\train\\image_dev_01.jpg", img2_path="img\\test\\image_dhruv_test_02.jpg")
print(verification)
end = datetime.datetime.now()

print("Time taken : ", end - start)