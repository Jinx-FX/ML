import cv2 as cv


def keys_demo():
    image = cv.imread("test/test.png")  # BGR, 0~255
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("input", image)
    while True:
        c = cv.waitKey(1)  # 处理视频要为 “1”
        if c == 49:  # 1
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            cv.imshow("result", gray)
        if c == 50:  # 2
            hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
            cv.imshow("result", hsv)
        if c == 51:  # 3
            invert = cv.bitwise_not(image)
            cv.imshow("result", invert)
        if c == 27:
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    keys_demo()
