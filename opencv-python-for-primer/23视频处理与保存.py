import cv2 as cv
import numpy as np

def video_demo():
    cap = cv.VideoCapture("test/balltest.mp4")
    w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv.CAP_PROP_FPS)
    out = cv.VideoWriter("test/out.mp4",  cv.CAP_ANY, np.int(cap.get(cv.CAP_PROP_FOURCC)), fps, (np.int(w), np.int(h)), True)
    print(w, h, fps)
    while True:
        ret, frame = cap.read()
        if ret is not True:
            break
        cv.imshow("frame", frame)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow("result", hsv)
        # out.write(hsv) # 保存视频
        c = cv.waitKey(10)
        if c == 27:
            break
    cv.destroyAllWindows()

    out.release()
    cap.release()

if __name__ == "__main__":
    video_demo()