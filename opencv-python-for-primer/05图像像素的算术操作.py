import cv2 as cv
import numpy as np

def math_demo():
    image = cv.imread("test/test.png")
    cv.imshow("input", image)
    
    blank = np.zeros_like(image)
    blank[:,:] = (50,50,50)

    # 进行四则运算
    # 图像的 大小 和 通道数 要保持一致
    # result = cv.add(image,blank)
    # result = cv.subtract(image,blank) # 减
    # result = cv.divide(image,blank) # 除
    result = cv.multiply(image,blank) # 乘

    cv.imshow("result", result)
    cv.imshow("blank",blank)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    math_demo()