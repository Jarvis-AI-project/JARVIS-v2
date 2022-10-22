from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

face_client = FaceClient("https://facialrecognition244.cognitiveservices.azure.com/",
                         CognitiveServicesCredentials("cba050788d4e4e69aa869ee84cb6c9e6"))

face_client.person_group.create(person_group_id="test", name="test")