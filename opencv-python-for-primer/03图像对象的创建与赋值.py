# 一切图像皆是 numpy

import cv2 as cv
import numpy as np


def mat_demo():
    image = cv.imread("test/test.png")
    print(image.shape)  # H, W, C:高度，宽度，颜色

    # 拷贝图像的某一区域
    # roi = image[100:200, 100:200, :]

    # # blank 是与 image 大小相同的空白图像
    # blank = np.zeros_like(image)

    # 也可以这样拷贝一片空白区域
    # h,w,c = image.shape
    # blank = np.zeros((h,w,c),dtype = np.uint8)

    # 拷贝某一区域
    # # 若 image 是灰度图像， 就没有第三个 “:”
    # blank[100:200, 100:200, :] = image[100:200, 100:200, :]

    # 拷贝图像
    blank = np.copy(image)
    # 或 .但这一种 即相当于两个变量的数据存储在相同的地址，改变 blank 即改变 image
    # blank = image

    cv.imshow("blank", blank)
    # cv.imshow("roi", roi)
    cv.imshow("input", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    mat_demo()

