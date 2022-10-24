import cv2
video_stream = cv2.VideoCapture(0)

while video_stream.isOpened():
    (_, frame_raw) = video_stream.read()
    frame = cv2.flip(frame_raw, 1)
    cv2.imshow('FaceID Verification', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        video_stream.release()
        cv2.destroyAllWindows()
        print('FaceID: Quit')
