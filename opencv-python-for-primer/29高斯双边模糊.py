import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def bifilter_demo():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)
    result = cv.bilateralFilter(image, 0, 100, 10)
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    bifilter_demo()