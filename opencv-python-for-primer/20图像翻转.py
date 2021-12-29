import cv2 as cv
import numpy as np

def flip_demo():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)
    cv.namedWindow("flip", cv.WINDOW_AUTOSIZE)
    # 1：左右翻转，0：原点对称翻转，-1：上下翻转
    dst = cv.flip(image, -1) 
    cv.imshow("flip", dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    flip_demo()