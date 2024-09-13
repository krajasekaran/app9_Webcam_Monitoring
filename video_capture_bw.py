import cv2
import time
from sending_email import send_email

video = cv2.VideoCapture(1)
time.sleep(1)

first_frame = None
status_list = []

while True:
    status = 0
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # this will cover the pic to grey scale with blurred image
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = grey_frame_gau

    # to find the difference in the frame
    delta_frame = cv2.absdiff(grey_frame_gau, first_frame)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("sample", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        if rectangle.any():
            # logic to check the entry and exit of an object
            status = 1
            send_email()
    # we are appending the status_list with 0's and 1's as the object enters and exits
    status_list.append(status)
    # we are monitoring the last two items of the status_list and checking for the exit of the object
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        # send email when the object has exited the frame
        send_email()
    print(status_list)

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
