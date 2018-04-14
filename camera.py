import cv2
# create a capture
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
#
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(320,240))
while True:
  ret,frame = cap.read()
  print(str(ret))
  cv2.imshow("frame",frame)
  if cv2.waitKey(1) & 0xff == ord('q'):
      break
cap.release()
out.release()
cv2.destroyAllWindows()