import cv2
import numpy as np

#kartinka = cv2.imread("chel.png")
kartinka = cv2.imread("kap.jpg")
resized = cv2.resize(kartinka,(800,600))
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

cv2.imshow("original", resized)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist = 1, param1 = 30, param2 = 60, minRadius = 4, maxRadius = 50)

if circles is not None:
    circles = np.uint16(np.around(circles))[0]

    for (x,y,r) in circles:
        cv2.circle(resized, (x,y), r, (0,0,255), 2)
        cv2.circle(resized, (x,y), 2, (0,0,255), 2)

cv2.imshow("okoshko",resized)
cv2.waitKey(0)