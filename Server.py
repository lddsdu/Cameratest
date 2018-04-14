from Camera import Camera
import cv2
import os
import time

if __name__ == '__main__':
    os.chdir("/home/jack/Desktop/pic")
    camera = Camera()
    index = 0
    camera.initialize()

    time.sleep(1)

    while True:
        frame = camera.frame
        cv2.imwrite("pic%05d.png"%index,frame)
        index += 1
        time.sleep(1.0/6)