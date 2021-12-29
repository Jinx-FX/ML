import cv2 as cv

def color_space_demo():
    image = cv.imread("test/test.png")  # BRG 色彩空间, 0-255
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    # cv.nameWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("gray", gray)
    cv.imshow("hsv", hsv)
    cv.waitKey(0)
    cv.destoryAllWindows()

if __name__ == "__main__":
    color_space_demo()

