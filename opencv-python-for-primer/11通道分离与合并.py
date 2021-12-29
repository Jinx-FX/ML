import cv2 as cv
import numpy as np

def channels_split_demo():
    b1 = cv.imread("test/test.png")
    print(b1.shape)
    cv.imshow("input", b1)
    cv.imshow("b1", b1[:,:,2]) # 第二个通道

    mv = cv.split(b1)
    mv[0][:,:] = 255
    result = cv.merge(mv)
    cv.imshow("result",result)

    dst = np.zeros(b1.shape, dtype=np.uint8)
    cv.mixChannels([b1], [dst], fromTo=[2, 0, 1, 1, 0, 2]) # 改变通道
    cv.imshow("output4", dst)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    channels_split_demo()