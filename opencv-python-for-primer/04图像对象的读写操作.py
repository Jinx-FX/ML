import cv2 as cv
import numpy as np

def pixel_demo():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)

    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            b,g,r = image[row, col]
            # 取反色
            image[row, col] = (255-b, 255-g, 255-r)
    cv.imshow("result", image)

    cv.waitKey(0)
    cv.destroyAllWindows()

    # 保存
    # cv.imwrite("test_result.png", image)

if __name__ =="__main__":
    pixel_demo()