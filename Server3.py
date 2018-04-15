"""

contact via socket

"""

from Camera import Camera

from flask import Flask,render_template,request,Response,send_file
import cv2
import time
import socket
import pickle
import threading

server = socket.socket()
server.bind(("127.0.0.1",9999))
server.listen(5)
camera = Camera()
camera.initialize()

# wait the camera to capture the frame
time.sleep(1)

index = 0

def serve(conn):
    while True:
        frame = camera.frame
        byte_frame = pickle.dumps(frame)
        try:
            conn.send(b'startTag' + byte_frame + b'endTag')
        except Exception:
            print("one client stopped")
            break
        time.sleep(1.0 / 6)

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    t = threading.Thread(target=serve, args=(conn,))
    t.start()



# if __name__ == '__main__':
    # app.run(port=10086,host="172.25.190.138")