import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def image_hist():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [32], [0, 256])
        print(hist)
        plt.plot(hist, color=color)
        plt.xlim([0, 32])
    plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    image_hist()