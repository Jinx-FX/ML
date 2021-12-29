import cv2 as cv
import numpy as np

b1 = cv.imread("test/test.png")  # np.zeros((512, 512, 3), dtype=np.uint8)
img = np.copy(b1)
x1 = -1
x2 = -1
y1 = -1
y2 = -1
def mouse_drawing(event, x, y, flags, param):
    global x1, y1, x2, y2
    if event == cv.EVENT_LBUTTONDOWN: # 鼠标左键按下
        x1 = x
        y1 = y
    if event == cv.EVENT_MOUSEMOVE: # 鼠标移动
        if x1 < 0 or y1 < 0:
            return
        x2 = x
        y2 = y
        dx = x2 - x1
        dy = y2 - y1
        if dx > 0 and dy > 0:
            b1[:,:,:] = img[:,:,:]
            cv.rectangle(b1, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
    if event == cv.EVENT_LBUTTONUP: # 鼠标抬起
        x2 = x
        y2 = y
        dx = x2 - x1
        dy = y2 - y1
        if dx > 0 and dy > 0:
            b1[:, :, :] = img[:,:,:] #reset
            cv.rectangle(b1, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
        x1 = -1
        x2 = -1
        y1 = -1
        y2 = -1

def mouse_demo():
    cv.namedWindow("mouse_demo", cv.WINDOW_AUTOSIZE)
    cv.setMouseCallback("mouse_demo", mouse_drawing) # 回调函数
    while True:
        cv.imshow("mouse_demo", b1)
        c = cv.waitKey(10)
        if c == 27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    mouse_demo()