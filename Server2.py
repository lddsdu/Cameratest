from Camera import Camera
from flask import Flask,render_template,request,Response,send_file
import cv2
import time


camera = Camera()
camera.initialize()

# wait the camera to capture the frame
time.sleep(1)

index = 0

# the app here is an Object
app = Flask(__name__)

@app.route('/getpic')
def getpic():
    global index
    index += 1
    return send_file("/home/jack/Desktop/pic/pic00000.png","image/png")

@app.route('/getvideo')
def getVideo():
    """video streaming route"""
    return Response(gen(camera),mimetype="multipart/x-mixed-replace;boundary=frame")

def gen(camera):
    while True:
        frame= camera.frame
        # how to change  frame(ndarry) to binary info
        temp = cv2.imwrite("/tmp/a.png",frame)
        sendfile = open("/tmp/a.png","rb+")
        send = sendfile.read()
        sendfile.close()
        yield (b'--frame\r\n' 
               b'Content-Type: image/png\r\n\r\n' + send + b'\r\n')
        time.sleep(1.0/6)

if __name__ == '__main__':
    app.run(port=10086,host="172.25.190.138")