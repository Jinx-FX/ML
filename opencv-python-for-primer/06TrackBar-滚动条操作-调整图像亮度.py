import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

def adjust_lightness_demo():
    image = cv.imread("test/test.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("lightness", "input", 0, 250, nothing)  # 0-100 表示亮度调节的范围,最高 250 全白
    cv.imshow("input", image)
    blank = np.zeros_like(image)
    while True:
        pos = cv.getTrackbarPos("lightness","input")
        blank[:,:] = (pos,pos,pos)
        result = cv.add(image,blank)

        cv.imshow("result", result)
        c = cv.waitKey(1)
        if c == 27: # 27 为 esc 键
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    adjust_lightness_demo()