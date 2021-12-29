import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def blur_demo():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)
    result = cv.blur(image, (15, 15)) # 卷积矩阵
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    blur_demo()