import cv2 as cv
import numpy as np

def pixel_stat_demo():
    b1 = cv.imread("test/test.png")
    print(b1.shape)
    cv.imshow("input", b1)
    # 最大值
    print(np.max(b1[:,:,2]))
    # 均值和方差
    means, dev = cv.meanStdDev(b1)
    print("means:\n", means)
    print("dev\n", dev)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    pixel_stat_demo()