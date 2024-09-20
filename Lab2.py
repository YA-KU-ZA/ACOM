import cv2
import numpy as np

def main():
    # Инициализация камеры
    cap = cv2.VideoCapture(0)

    while True:
        # Чтение кадра с камеры
        ret, frame = cap.read()

        if not ret:
            break

        #Задание 1
        # Преобразование в HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Задание 2
        # Диапазон для красного цвета в HSV
        lower_red = np.array([0, 48, 80])
        upper_red = np.array([20, 255, 255])

        # Создание маски для красного цвета
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Применение маски к исходному изображению
        result = cv2.bitwise_and(frame, frame, mask=mask)

        #Задание 3
        # Морфологические преобразования
        kernel = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

        #Задание 4-5
        # Поиск контуров и вычисление моментов
        contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Создание копии исходного кадра для рисования
        drawing_frame = frame.copy()

        for contour in contours:
            moments = cv2.moments(contour)
            area = moments['m00']

            if area > 1000:  # Фильтрация по площади
                x, y, w, h = cv2.boundingRect(contour)

                # Построение прямоугольника вокруг объекта
                cv2.rectangle(drawing_frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

                # Вывод информации о площади
                cv2.putText(drawing_frame, f'Area: {int(area)}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (0, 0, 0), 2)

        # Вывод результатов на несколько окон
        cv2.imshow('Original', frame)
        cv2.imshow('HSV', hsv)
        cv2.imshow('Mask', mask)
        cv2.imshow('Result', result)
        cv2.imshow('Opening', opening)
        cv2.imshow('Closing', closing)
        cv2.imshow('Final Result', drawing_frame)

        # Ожидание нажатия клавиши 'q' для выхода из цикла
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()