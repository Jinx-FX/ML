import cv2 as cv
import numpy as np

def nothing(x):
    print(x)

def adjust_contrast_demo():
    image = cv.imread("test/test.png")
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("lightness", "input", 0, 100, nothing)
    cv.createTrackbar("contrast", "input", 100, 200, nothing)
    cv.imshow("input", image)
    blank = np.zeros_like(image)
    while True:
        # 设置传递的 亮度 和 对比度 值
        lightness = cv.getTrackbarPos("lightness","input")
        contrast = cv.getTrackbarPos("contrast", "input") / 100
        print("lightness:",lightness,"contrast",contrast)
        # 相当于增加权重
        result = cv.addWeighted(image, contrast, blank, 0.5, lightness)

        cv.imshow("result", result)
        c = cv.waitKey(1)
        if c == 27: # 27 为 esc 键
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    adjust_contrast_demo()