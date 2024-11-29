import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Gauss {
    public static void main(String[] args) throws IOException {

        BufferedImage image = ImageIO.read(new File("D:/Raspred/MPJ_REST/src/photo_2024-09-06_15-58-59.jpg"));

        BufferedImage blur1 = gaussianBlur(image, 3, 100);
        BufferedImage blur2 = gaussianBlur(image, 3, 10);
        BufferedImage blur3 = gaussianBlur(image, 5, 100);
        BufferedImage blur4 = gaussianBlur(image, 5, 10);
        BufferedImage blur5 = gaussianBlur(image, 7, 100);
        BufferedImage blur6 = gaussianBlur(image, 7, 10);

        displayImage(image, "Original");
        displayImage(blur1, "Kernel size 3 | Standard deviation 100");
        displayImage(blur2, "Kernel size 3 | Standard deviation 10");
        displayImage(blur3, "Kernel size 5 | Standard deviation 100");
        displayImage(blur4, "Kernel size 5 | Standard deviation 10");
        displayImage(blur5, "Kernel size 7 | Standard deviation 100");
        displayImage(blur6, "Kernel size 7 | Standard deviation 10");
    }

    // Метод для применения Гауссова размытия
    public static BufferedImage gaussianBlur(BufferedImage image, int kernelSize, double stdDeviation) {
        int width = image.getWidth(); // Получение ширины изображения
        int height = image.getHeight(); // Получение высоты изображения
        // Создание нового изображения для хранения результата
        BufferedImage result = new BufferedImage(width, height, image.getType());

        int radius = kernelSize / 2; // Вычисление радиуса ядра
        double[][] kernel = new double[kernelSize][kernelSize]; // Инициализация ядра
        double sum = 0.0; // Переменная для суммы значений ядра

        // Генерация Гауссового ядра
        for (int i = 0; i < kernelSize; i++) {
            for (int j = 0; j < kernelSize; j++) {
                // Вычисление значения Гауссова ядра
                kernel[i][j] = gauss(i - radius, j - radius, stdDeviation);
                sum += kernel[i][j];
            }
        }

        // Нормализация ядра
        for (int i = 0; i < kernelSize; i++) {
            for (int j = 0; j < kernelSize; j++) {
                kernel[i][j] /= sum;
            }
        }

        // Применение Гауссова ядра к изображению
        for (int x = radius; x < width - radius; x++) {
            for (int y = radius; y < height - radius; y++) {
                double value = 0; // Переменная для расчета нового значения пикселя
                for (int k = -radius; k <= radius; k++) {
                    for (int l = -radius; l <= radius; l++) {
                        // Получение цвета пикселя и умножение на соответствующее значение ядра
                        value += new Color(image.getRGB(x + k, y + l)).getRed() * kernel[k + radius][l + radius];
                    }
                }
                // Приведение значения к диапазону [0, 255] и создание нового цвета
                int intValue = Math.min(Math.max((int)value, 0), 255);
                Color newColor = new Color(intValue, intValue, intValue); // Создаем оттенок серого
                result.setRGB(x, y, newColor.getRGB()); // Устанавливаем новый цвет пикселя в результирующее изображение
            }
        }
        return result; // Возвращаем размытое изображение
    }

    // Метод для вычисления значения Гаусса
    public static double gauss(int x, int y, double omega) {
        return 1 / (2 * Math.PI * omega * omega) * Math.exp(-((x * x + y * y) / (2 * omega * omega)));
    }

    // Метод для отображения изображения в новом окне
    public static void displayImage(BufferedImage img, String title) {
        JFrame frame = new JFrame(title);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(img.getWidth(), img.getHeight());
        frame.add(new JLabel(new ImageIcon(img))); // Добавление изображения в окно
        frame.pack();
        frame.setVisible(true);
    }
}
