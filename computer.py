import cv2
import time
video_capture = cv2.VideoCapture(0)
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Detecting camera...')
time.sleep(20)
writer = cv2.VideoWriter('myvideo.mp4',cv2.VideoWriter_fourcc(*'XVID'),20,(width,height))
while(video_capture.isOpened()):
    re, frame = video_capture.read()

    if re:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        writer.write(frame)
        cv2.imshow('frame', frame)
    else:
        print('No camera detected.')

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()