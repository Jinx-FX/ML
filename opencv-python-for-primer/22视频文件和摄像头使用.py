import cv2 as cv
import numpy as np

def video_demo():
    cap = cv.VideoCapture("test/balltest.mp4")
    w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv.CAP_PROP_FPS)
    print(w, h, fps)
    while True:
        ret, frame = cap.read()
        if ret is not True:
            break
        cv.imshow("frame", frame)
        c = cv.waitKey(10)
        if c == 27:
            break
    cv.destroyAllWindows()

    cap.release()

if __name__ == "__main__":
    video_demo()