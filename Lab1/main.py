import cv2
import numpy as np


def main():
    # Задание 1: Вывод изображения
    print("\nЗадание 1: Вывод изображения")
    img = cv2.imread('photo_2024-09-06_15-58-59.jpg', cv2.IMREAD_COLOR)

    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 800, 600)
    cv2.imshow('Image', img)
    cv2.waitKey(2000)  # Пауза на 2 секунды

    # Тестирование разных расширений и флагов
    print("\nТестирование разных расширений и флагов")
    img_bgr = cv2.imread('photo_2024-09-06_15-58-59.jpg', cv2.IMREAD_COLOR)
    img_gray = cv2.imread('photo_2024-09-06_15-58-59.jpg', cv2.IMREAD_GRAYSCALE)
    img_unchanged = cv2.imread('photo_2024-09-06_15-58-59.jpg', cv2.IMREAD_UNCHANGED)

    cv2.namedWindow('Normal Window', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Auto Resize Window', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Fullscreen Window', cv2.WND_PROP_FULLSCREEN)

    cv2.imshow('Normal Window', img_bgr)
    cv2.imshow('Auto Resize Window', img_gray)
    cv2.imshow('Fullscreen Window', img_unchanged)

    cv2.waitKey(3000)  # Пауза на 3 секунды

    cv2.destroyAllWindows()

    # Задание 2: Отображение видео
    print("\nЗадание 2: Отображение видео")
    cap = cv2.VideoCapture('large.mp4')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        resized_frame = cv2.resize(frame, (640, 480))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Original Video', resized_frame)
        cv2.imshow('Grayscale Video', gray_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Задание 3: Запись видео из файла в другой файл
    print("\nЗадание 3: Запись видео из файла в другой файл")
    cap = cv2.VideoCapture('large.mp4')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_GRAY2BGR)

        out.write(processed_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Задание 4: Преобразование изображения в HSV и отображение
    print("\nЗадание 4: Преобразование изображения в HSV и отображение")
    img = cv2.imread('photo_2024-09-06_15-58-59.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)

    cv2.imshow('Original Image', img)
    cv2.imshow('HSV Image', hsv_img)

    cv2.waitKey(3000)  # Пауза на 3 секунды

    cv2.destroyAllWindows()

    print("\nЗадание 5 и 6: Изображение с камеры и красный крест")
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter('camera_video.mp4', fourcc, fps, (width, height))
    while True:
        # Чтение кадра с камеры
        ret, frame = cap.read()

        if not ret:
            break

        # Получение размеров кадра
        height, width, _ = frame.shape

        # Вычисление координат центра
        center_x = int(width / 2)
        center_y = int(height / 2)
        # Рисование красного креста
        cv2.line(frame, (center_x - 50, center_y - 10 ), (center_x + 50, center_y - 10), (0, 0, 255), 5)
        cv2.line(frame, (center_x - 50, center_y + 10), (center_x + 50, center_y + 10), (0, 0, 255), 5)
        cv2.line(frame, (center_x - 50, center_y - 10), (center_x - 50, center_y + 10), (0, 0, 255), 5)
        cv2.line(frame, (center_x + 50, center_y - 10), (center_x + 50, center_y + 10), (0, 0, 255), 5)
        cv2.line(frame, (center_x - 10, center_y + 10), (center_x - 10, center_y + 80), (0, 0, 255), 5)
        cv2.line(frame, (center_x - 10, center_y - 10), (center_x - 10, center_y - 80), (0, 0, 255), 5)
        cv2.line(frame, (center_x + 10, center_y - 10), (center_x + 10, center_y - 80), (0, 0, 255), 5)
        cv2.line(frame, (center_x + 10, center_y + 10), (center_x + 10, center_y + 80), (0, 0, 255), 5)
        cv2.line(frame, (center_x - 10, center_y - 80), (center_x + 10, center_y - 80), (0, 0, 255), 5)
        cv2.line(frame, (center_x - 10, center_y + 80), (center_x + 10, center_y + 80), (0, 0, 255), 5)
        #Еще можно было сделать крест через 3 квадрата, но я не ищу легких путей))))

        # Отображение кадра
        cv2.imshow('Camera', frame)
        out.write(frame)
        # Проверка клавиши выхода
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("\nЗадание 7 и 8: закраска креста")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape
        center_x, center_y = int(width / 2), int(height / 2)

        # Получаем цвет центрального пикселя
        b, g, r = frame[center_y, center_x]

        # Определяем доминирующий цвет
        dominant_color = max((r, 'red'), (g, 'green'), (b, 'blue'))[1]

        # Устанавливаем цвет в зависимости от доминирующего цвета
        color = {
            'red': (0, 0, 255),
            'green': (0, 255, 0),
            'blue': (255, 0, 0)
        }[dominant_color]

        vertices = np.array([
            [center_x - 10, center_y - 80],
            [center_x + 10, center_y - 80],
            [center_x + 10, center_y + 10],
            [center_x + 50, center_y + 10],
            [center_x + 50, center_y - 10],
            [center_x + 10, center_y - 10],
            [center_x + 10, center_y + 80],
            [center_x - 10, center_y + 80],
            [center_x - 10, center_y + 10],
            [center_x - 50, center_y + 10],
            [center_x - 50, center_y - 10],
            [center_x - 10, center_y - 10]
        ])

        # Рисуем и заполняем крест
        cv2.fillPoly(frame, pts=[vertices], color=color)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("\nЗадание 9: трансляция с телефона")

    # URL видеопотока из IP Webcam
    #url = "https://192.168.0.101:8080/video"
    # Создаем объект VideoCapture с URL видеопотока
    video = cv2.VideoCapture("https://192.168.0.101:8080/video")
    # Создаем окно с возможностью изменения размера
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    # Задаем желаемый размер окна
    cv2.resizeWindow('img', 800, 600)
    while True:
        ok, img = video.read()
        if not ok:
            print("Ошибка чтения кадра")
            break
        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
