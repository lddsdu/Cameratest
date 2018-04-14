"""



"""
import time
import socket
import pickle
import cv2

client = socket.socket()
client.connect(("127.0.0.1",9999))

class NdarrayParser:
    def __init__(self,startTag,endTag):
        self.startTag = startTag
        self.endTag = endTag
        self.buffer = b""
        self.byte_startTag = startTag.encode("utf8")
        self.byte_endTag = endTag.encode("utf8")

    def getFrame(self, subsquent):
        """
        :param subsquent:
        :return:
        """
        if(len(subsquent) != 0):
            self.buffer += subsquent
        s = self.buffer.find(self.startTag.encode("utf8"))
        e = self.buffer.find(self.endTag.encode("utf8"))
        if(e == -1 or s == -1):
            time.sleep(0.01)
            return
#       find a frame
        print("find a new frame!!!")
        pickled_frame = self.buffer[s + len(self.byte_startTag):e]
        frame = pickle.loads(pickled_frame)
        cv2.imshow("frame",frame)
        cv2.waitKey(1)
        self.buffer = self.buffer[e+len(self.byte_endTag):(len(self.buffer))]

class Parser:
    """
    read a byte list and get a numpy.ndarray Object
    """
    bytearray = []

    def __init__(self,startTag,endTag):
        self.startTag = startTag
        self.endTag = endTag

    def append(self,bytearay):
        bytearray.append(bytearray)

    def readFrame(self):
        """
        try to read a frame
        :return:
        """
        pass

while True:
    """
    get 1024 byte size most
    """
    ndarrayParser = NdarrayParser("startTag","endTag")
    while True:
        res = client.recv(1024 * 1024)
        ndarrayParser.getFrame(res)




