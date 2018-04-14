import cv2
from time import time
# load the picture
im = cv2.imread("/home/jack/Desktop/a.png")

# change the color BGR to gray
im2 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

# plot the origin pic
cv2.imshow("origin",im)

# plot the gray pic
cv2.imshow("gray",im2)