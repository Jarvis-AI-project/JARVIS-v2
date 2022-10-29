import cv2
import time
from threading import Thread
from compreface import CompreFace
import functions.FaceRecognition.get_host as get_host
import os, sys

def FaceID():
    #SERVER -LOCAL
    # api_key, host, port = 'd742b38d-d659-404d-bde4-db41c67a50dd', 'http://192.168.1.7', 8080

    #SERVER - REMOTE
    hostt = get_host.get_host()
    if hostt != False:
        host = hostt
    else:
        return False
    api_key, port = 'd742b38d-d659-404d-bde4-db41c67a50dd', ''

    # LOCALHOST
    # api_key, host, port = '85b979c0-5b59-4112-a798-8092053041ca', 'http://localhost', '8000'

    try:
        video_stream = cv2.VideoCapture(0)
        video_stream.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        compre_face = CompreFace(host, port, {
            "limit": 0,
            "det_prob_threshold": 0.8,
            "prediction_count": 1,
            "status": True
        })

        recognition = compre_face.init_face_recognition(api_key)
        print('FaceID: Thread started')
        while video_stream.isOpened():
            (_, frame_raw) = video_stream.read()
            frame = cv2.flip(frame_raw, 1)
            try:
                _, im_buf_arr = cv2.imencode(".jpg", frame)
            except Exception as e:
                print('OpenCV - Your Camera is being used by another program.')
                print(e)
                return False

            byte_im = im_buf_arr.tobytes()
            data = recognition.recognize(byte_im)
            results = data.get('result')

            for result in results if results != None else []:
                if (result['subjects'][0]['subject'] == 'Devasheesh' or result['subjects'][0]['subject'] == 'Dhruv') and result['subjects'][0]['similarity'] >= 0.98:
                    print('FaceID Person: {}'.format(
                        result['subjects'][0]['subject']))
                    print('FaceID Similarity: {}'.format(
                        result['subjects'][0]['similarity']))
                    print('FaceID Execution Time: {}'.format(
                        result['execution_time']))
                    video_stream.release()
                    cv2.destroyAllWindows()
                    return True
                else:
                    print('Unknown Person')

            #cv2.imshow('FaceID Verification', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                video_stream.release()
                cv2.destroyAllWindows()
                print('FaceID: Quit')
                return False
    except Exception as e:
        print('FaceID: Error')
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type,  fname,  exc_tb.tb_lineno)
        return False


if __name__ == '__main__':
    FaceID()