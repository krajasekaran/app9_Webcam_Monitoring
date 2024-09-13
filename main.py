# pip install opencv-python
import cv2
import time

# 0 doesn't get access to mac camera
video = cv2.VideoCapture(1)
check, frame = video.read()
time.sleep(1)

check1, fame1 = video.read()
time.sleep(2)

check2, frame2 = video.read()
# the below line check the camera access
print(check)
# we print frame2 to make sure that camera can get some images
print(frame2)
