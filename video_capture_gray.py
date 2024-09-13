import cv2
import time


def video_capture():
    video = cv2.VideoCapture(1)
    time.sleep(1)

    while True:
        check, frame = video.read()
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)
        cv2.imshow("sample", grey_frame_gau)

        key = cv2.waitKey(1)

        if key == ord("q"):
            break

    video.release()