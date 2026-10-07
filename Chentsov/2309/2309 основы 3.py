# 1. Основы
#качаем фотку кота, качаем фотку геометрических фигур
#называем cat.jpg и shapes.png
#Ctrl + Shift + P > Python: Select Interpreter > Recommended
#устанавливаем Ctrl + ``: python -m pip install opencv-python

import cv2  # Импортируем библиотеку OpenCV
#
image = cv2.imread("cat.jpg")
resized_image = cv2.resize(image, (640,480))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5,5), 0)
cat_face = resized_image[100:200, 180:360]
#help(cv2.imread) - узнать про метод imread модуля cv2

##################print(image)- печатаем ПРЯМ МАТРИЦУ


# Узнать разрешение картинки и количество каналов цвета
# Выведет, например: (400, 500, 3) -> Высота 400px, Ширина 500px, 3 канала (B, G, R)
print("Размер изображения:", image.shape)

# Узнать тип данных, из которых состоят пиксели
# Выведет: uint8 -> это означает "целые числа от 0 до 255"
print("Тип данных пикселей:", image.dtype)

# Посмотреть цвет самого первого пикселя в самом верхнем левом углу (строка 0, колонка 0)
print("Цвет пикселя (0,0):", image[0, 0])

## 2. Обработка
cv2.imshow("Original cat", image)
cv2.waitKey(1000)
cv2.destroyWindow("Original cat")
cv2.imshow("Resized cat", resized_image)
cv2.waitKey(1000)
cv2.destroyWindow("Resized cat")
#ЧБ - самая популярное и важное редактирование
cv2.imshow("Gray resized cat", gray_image)
cv2.waitKey(1000)
cv2.destroyWindow("Gray resized cat")
# Это нужно, чтобы убрать мелкий «шум» (лишние детали), который мешает искать контуры
cv2.imshow("Blurry cat", blurred_image)
cv2.waitKey(1000)
cv2.destroyWindow("Blurry cat")

cv2.imshow("Face cat", cat_face)
cv2.waitKey(9000)
cv2.destroyWindow("Face cat")
#Окно закроется мгновенно. Потому что программа выполнилась.

#cv2.destroyAllWindows()

#Закрываем не через крестик, а нажатием клавиши или через время
# 0 - колво миллисекунд
# 5000 - 5 секунд
# 0 - бесконечное колво

# Самостоятельное задание на подумать: как сделать закрытие на "q"? Поч?

#Окно огромное, делаем меньше


## На входе должно быть строго серое изображение (gray_image)
# Параметры: (картинка, порог_яркости, максимальное_значение, тип_фильтра)
# Если пиксель темнее 127 -> он станет 0 (черным). Если ярче 127 -> станет 255 (белым).
########ret, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

########cv2.imshow("Binary Threshold", threshold_image)
########cv2.waitKey(0)

##
# Способ 1: Сделать «негатив» картинки (инверсия)
# Из максимальной яркости 255 вычитается текущее значение каждого пикселя
#inverted_image = 255 - resized_image
#cv2.imshow("Inverted Cat", inverted_image)
#cv2.waitKey(0)

# Способ 2: Осветлить картинку (прибавить яркость)
# Но будь аккуратен: обычный плюс в Python может вызвать "переполнение" (250 + 10 станет 4)
# Поэтому в OpenCV используют безопасную функцию:
#bright_image = cv2.add(resized_image, (50, 50, 50, 0)) # Прибавили по 50 единиц к B, G и R каналам
#cv2.imshow("Bright Cat", bright_image)
#cv2.waitKey(0)
##