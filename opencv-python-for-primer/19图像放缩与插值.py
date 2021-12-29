import cv2 as cv
import numpy as np

def resize_demo():
    image = cv.imread("test/test.png")
    h, w, c = image.shape
    cv.namedWindow("resize", cv.WINDOW_AUTOSIZE)
    dst = cv.resize(image, (0, 0), fx=0.75, fy=0.75, interpolation=cv.INTER_NEAREST) # 插值方式
    cv.imshow("resize", dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    resize_demo()