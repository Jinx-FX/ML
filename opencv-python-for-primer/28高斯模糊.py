import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def conv_demo():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)
    result = cv.GaussianBlur(image, (0, 0), 15) # 若大于 0 ，必须是奇数
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    conv_demo()