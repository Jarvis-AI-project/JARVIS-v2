import cv2
import time
from threading import Thread
from compreface import CompreFace
from compreface.service import RecognitionService

api_key = '85b979c0-5b59-4112-a798-8092053041ca'
host = 'http://localhost'
port = '8000'


class ThreadedCamera:
    def __init__(self):
        self.active = True
        self.results = []
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        compre_face: CompreFace = CompreFace(host, port, {
            "limit": 0,
            "det_prob_threshold": 0.8,
            "prediction_count": 1,
            "status": True
        })

        self.recognition: RecognitionService = compre_face.init_face_recognition(api_key)

        self.FPS = 1/20

        # Start frame retrieval thread
        self.thread = Thread(target=self.show_frame, args=())
        self.thread.daemon = True
        self.thread.start()

    def show_frame(self):
        print('FaceID: Thread started')
        while self.capture.isOpened():
            (status, frame_raw) = self.capture.read()
            self.frame = cv2.flip(frame_raw, 1)

            if self.results:
                results = self.results
                for result in results:
                    box = result.get('box')
                    subjects = result.get('subjects')
                    if box:
                        cv2.rectangle(img=self.frame, pt1=(box['x_min'], box['y_min']),
                                      pt2=(box['x_max'], box['y_max']), color=(0, 255, 0), thickness=1)

                        if subjects:
                            subjects = sorted(
                                subjects, key=lambda k: k['similarity'], reverse=True)
                            subject = f"Subject: {subjects[0]['subject']}"
                            if 'devasheesh' in (subject.lower()).strip():
                                print('FaceID: Devasheesh')
                                return
                                
                            similarity = f"Similarity: {subjects[0]['similarity']}"
                            cv2.putText(self.frame, subject, (box['x_max'], box['y_min'] + 75),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                            cv2.putText(self.frame, similarity, (box['x_max'], box['y_min'] + 95),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
                        else:
                            subject = f"No known faces"
                            cv2.putText(self.frame, subject, (box['x_max'], box['y_min'] + 75),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

            #cv2.imshow('JARVIS FaceID', self.frame)
            time.sleep(self.FPS)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.capture.release()
                cv2.destroyAllWindows()
                self.active = False







    def is_active(self):
        return self.active

    def update(self):
        if not hasattr(self, 'frame'):
            return

        _, im_buf_arr = cv2.imencode(".jpg", self.frame)
        byte_im = im_buf_arr.tobytes()
        data = self.recognition.recognize(byte_im)
        self.results = data.get('result')



threaded_camera = ThreadedCamera()
while threaded_camera.is_active():
    threaded_camera.update()