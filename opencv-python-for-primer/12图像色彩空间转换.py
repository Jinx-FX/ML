import cv2 as cv
import numpy as np

def color_space_demo():
    b1 = cv.imread("test/greenback.png")
    print(b1.shape)
    cv.imshow("input", b1)
    hsv = cv.cvtColor(b1, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    
    # 类似抠图，分离出对应区域和颜色,绿色一般最好处理
    mask = cv.inRange(hsv, (35, 43, 46), (77, 255, 255))
    cv.bitwise_not(mask, mask) # 取反，使取需要取的图大于0
    result = cv.bitwise_and(b1, b1, mask=mask)
    
    cv.imshow("result", result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    color_space_demo()