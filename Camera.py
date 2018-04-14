import cv2
import time
import threading

class Camera():
    frame = None
    thread = None
    # capture set
    cap = cv2.VideoCapture(1)
    cap.set(3,640)
    cap.set(4,480)

    def initialize(self):
        if Camera.frame == None:
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

    def _thread(self):
        while True:
            ret,frame = Camera.cap.read()
            if ret:
                Camera.frame = frame
            time.sleep(1.0/6)