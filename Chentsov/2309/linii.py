import cv2
import numpy as np

#kartinka = cv2.imread("chel.png")
kartinka = cv2.imread("kap.jpg")
resized = cv2.resize(kartinka,(800,600))
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 20, 100)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold = 1, minLineLength = 1, maxLineGap = 5)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line.ravel()
        cv2.line(resized, (x1,y1), (x2,y2), (255,255,0), 1)

cv2.imshow("okoshko2",edges)
cv2.imshow("okoshko3",resized)
cv2.waitKey(0)