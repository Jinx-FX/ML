import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def eqhist_demo():
    image = cv.imread("test/test.png", cv.IMREAD_GRAYSCALE)
    cv.imshow("input", image)
    result = cv.equalizeHist(image) # "灰度"图像的均衡化
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    eqhist_demo()