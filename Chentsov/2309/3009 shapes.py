import cv2
import numpy as np

kartinka = cv2.imread("fig.jpeg")
gray = cv2.cvtColor(kartinka, cv2.COLOR_BGR2GRAY)
blurry = cv2.GaussianBlur(gray,(1,1),0)
_, thresh = cv2.threshold(blurry, 160, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


for contour in contours:
    if cv2.contourArea(contour) < 100:
        continue

    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
    vershini = len(approx)
    #
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    #
    if vershini == 3:
        shape_name = "Treygolnik"
    elif vershini == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        shape_name = "Kvadrat" if 0.95 <= aspect_ratio <= 1.05 else "Pryamoygolnik"
    elif vershini == 5:
        shape_name = "5golnik"
    else:
        shape_name ="krug"
    

    cv2.drawContours(kartinka, [approx], -1, (0, 255, 0), 2)
    cv2.putText(kartinka, shape_name, (cX, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
cv2.imshow("Final", thresh)
cv2.waitKey(0)