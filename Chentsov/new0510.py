import cv2
kartinka = cv2.imread("figu.png")
gray = cv2.cvtColor(kartinka, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5),0)
_, porog = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY_INV)
konturi, _ = cv2.findContours(porog.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for kontur in konturi:
    area = cv2.contourArea(kontur)
    if cv2.contourArea(kontur) < 100:
        continue
    peri = cv2.arcLength(kontur, True)
    approx = cv2.approxPolyDP(kontur, 0.04*peri, True)
    vershini = len(approx)

    x, y, w, h = cv2.boundingRect(approx)
    cX = x + w // 2
    cY = y + h //2

    if vershini == 3:
        shape_name = "treygolnik"
    elif vershini == 4:
        aspect_ratio = float(w)/h
        if 0.95 <= aspect_ratio <= 1.05:
            shape_name = "kvadrat"
        else:
            shape_name = "pryamoygolnik"
    elif vershini == 5:
        shape_name = "pyatiygolnik"
    else:
        shape_name = "krug"
    #print(vershini, shape_name)
    cv2.drawContours(kartinka,[approx], -1, (0,255,0), 5)
    text = f"{shape_name} (S:{int(area)})"
    cv2.putText(kartinka, text, (cX, cY), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 2)
cv2.imshow("okoshko", kartinka)
cv2.waitKey(0000)