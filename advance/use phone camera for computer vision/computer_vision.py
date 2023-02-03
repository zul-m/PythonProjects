import cv2
import numpy as np

url = "211.24.39.209"
cp = cv2.VideoCapture(url)

while(True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

cv2.destroyAllWindows()