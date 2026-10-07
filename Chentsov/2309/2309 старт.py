#Ctrl + Shift + P > Python: Select Interpreter > Recommended
#устанавливаем Ctrl + `: \
#python -m pip install opencv-python

import cv2  # Импортируем библиотеку OpenCV
babushka = cv2.imread("dog.jfif")

#print(babushka)
cv2.imshow("KARTINKA", babushka)
print('Размер изображения =', babushka.shape)
cv2.waitKey(0)
cv2.destroyWindow("KARTINKA")

resized_babushka = cv2.resize(babushka, (600,100))
cv2.imshow("SMESHNAYA KARTINKA", resized_babushka)
cv2.waitKey(0)
cv2.destroyWindow("SMESHNAYA KARTINKA")

gray_babushka = cv2.cvtColor(babushka, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY KARTINKA", gray_babushka)
cv2.waitKey(0)
cv2.destroyWindow("GRAY KARTINKA")

blurry_babushka = cv2.GaussianBlur(babushka, (15,15), 0)
cv2.imshow("BLURRY KARTINKA", blurry_babushka)
cv2.waitKey(0)
cv2.destroyWindow("BLURRY KARTINKA")

cropped_babushka = babushka[3:125, 150:270]
cv2.imshow("CROPPED KARTINKA", cropped_babushka)
cv2.waitKey(0)
cv2.destroyWindow("CROPPED KARTINKA")

cv2.destroyAllWindows()
