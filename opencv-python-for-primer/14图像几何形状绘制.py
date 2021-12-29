import cv2 as cv
import numpy as np

def drawing_demo():
    b1 = cv.imread("test/test.png")#np.zeros((512, 512, 3), dtype=np.uint8)
    temp = np.copy(b1)
    cv.rectangle(b1, (50, 50), (400, 400), (0, 0, 255), 4, 8, 0) # img，左上角，右上角……
    # cv.circle(b1, (200, 200), 100, (255, 0, 0), -1, 8, 0)
    # cv.line(b1, (50, 50), (400, 400), (0, 255, 0), 4, 8, 0)
    cv.putText(b1, "99% face", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2, 8) #（50，50）坐标
    cv.imshow("input", b1)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    drawing_demo()