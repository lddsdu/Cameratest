import threading
import pickle
from pickle_test import Person
import random
import time

startTag = "startTag"
endTag = "endTag"

bytearrays = b''
index = 0

def thr():
    """
    create a new frame
    :return:
    """
    while True:
        global index
        person = Person(name="jack%05d"%index,age=index,gender="male")
        print(">>>"+str(index))
        index += 1
        byte_data = pickle.dumps(person)
        global bytearrays
        bytearrays += (startTag.encode("utf8")) + byte_data +(endTag.encode("utf8"))
        time.sleep(1.0/6)

producer = threading.Thread(target=thr)
producer.start()
print("new thread")

class FrameParser:

    def __init__(self,startTag,endTag):
        self.startTag = startTag
        self.endTag = endTag
        self.sindex = 0
        self.eindex = 0

    def getFrame(self):
        while True:
            s = bytearrays.find(b"startTag",self.sindex)
            e = bytearrays.find(b"endTag",self.sindex)
            if s == -1 or e == -1:
                continue
                time.sleep(0.1)
            new = bytearrays[s+8:e]
            person = pickle.loads(new)
            person.intro()
            self.sindex = e + len(b"endTag")

    def getFrameByCut(self):
        while True:
            global bytearrays
            s = bytearrays.find(b"startTag",self.sindex)
            e = bytearrays.find(b"endTag",self.eindex)
            if(s == -1 or e == -1):
                continue
            new = bytearrays[s+8:e]
            person = pickle.loads(new)
            person.intro()
            bytearrays = bytearrays[e+7:len(bytearrays)]

frameparser = FrameParser(startTag,endTag)

while True:
    frameparser.getFrameByCut()