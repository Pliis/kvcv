import cv2
import mediapipe     as mp

# Инициализация модулей MediaPipe для распознавания рук
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Настройка модели распознавания
# max_num_hands=2 означает, что модель будет искать максимум две руки
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Запуск захвата видео с веб-камеры (0 — индекс встроенной камеры)
cap = cv2.VideoCapture(0)

print("Программа запущена. Нажмите 'q' для выхода.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Не удалось получить кадр с веб-камеры.")
        break

    # MediaPipe работает с цветами RGB, а OpenCV по умолчанию читает в BGR
    # Инвертируем кадр по горизонтали (зеркальное отображение) и меняем цвет
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Обработка кадра нейросетью
    results = hands.process(rgb_frame)

    # Если руки обнаружены, рисуем ключевые точки и связи
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Отрисовка скелета руки (21 ключевая точка)
            mp_drawing.draw_landmarks(
                frame, 
                hand_landmarks, 
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4), # Точки
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)  # Линии соединения
            )

    # Отображение окна с результатом
    cv2.imshow('Hand Tracking', frame)

    # Выход из цикла при нажатии на клавишу 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
hands.close()
