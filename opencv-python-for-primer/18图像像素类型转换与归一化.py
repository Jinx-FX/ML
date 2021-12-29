import cv2 as cv
import numpy as np

def norm_demo():
    image = cv.imread("test/test.png")
    cv.namedWindow("norm_demo", cv.WINDOW_AUTOSIZE)
    result = np.zeros_like(np.float32(image))
    cv.normalize(np.float32(image), result, 0, 1, cv.NORM_MINMAX, dtype=cv.CV_32F)
    cv.imshow("norm_demo", np.uint8(result*255))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    norm_demo()