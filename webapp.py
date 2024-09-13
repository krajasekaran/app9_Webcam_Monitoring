import time
import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    st_image = st.image([])
    video = cv2.VideoCapture(1)
    time.sleep(1)

    while True:

        now = datetime.now()
        check, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame,
                    text="Hello",
                    org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        cv2.putText(img=frame,
                    text=now.strftime("%A"),
                    org=(50, 100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        cv2.putText(img=frame,
                    text=now.strftime("%H:%M:%S"),
                    org=(50, 150),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        st_image.image(frame)


