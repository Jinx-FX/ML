import cv2 as cv
import numpy as np

def polyline_drawing_demo():
    canvas = np.zeros((512, 512, 3), dtype=np.uint8)
    pts = np.array([[100, 100], [350, 100], [450, 280], [320, 450], [80, 400]],  dtype=np.int32)
    # cv.fillPoly(canvas, [pts], (255, 0, 255), 8, 0); #填充
    # cv.polylines(canvas, [pts], True, (0, 0, 255), 2, 8, 0); #绘制
    cv.drawContours(canvas, [pts], -1, (255, 0, 0), -1); # 集合了上两个函数的功能
    cv.imshow("polyline", canvas);
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    polyline_drawing_demo()