import cv2 as cv


def color_table_demo():
    colormap = [
        cv.COLORMAP_AUTUMN,
        cv.COLORMAP_BONE,
        cv.COLORMAP_JET,
        cv.COLORMAP_WINTER,
        cv.COLORMAP_RAINBOW,
        cv.COLORMAP_OCEAN,
        cv.COLORMAP_SUMMER,
        cv.COLORMAP_SPRING,
        cv.COLORMAP_COOL,
        cv.COLORMAP_PINK,
        cv.COLORMAP_HOT,
        cv.COLORMAP_PARULA,
        cv.COLORMAP_MAGMA,
        cv.COLORMAP_INFERNO,
        cv.COLORMAP_PLASMA,
        cv.COLORMAP_VIRIDIS,
        cv.COLORMAP_CIVIDIS,
        cv.COLORMAP_TWILIGHT,
        cv.COLORMAP_TWILIGHT_SHIFTED]

    image = cv.imread("test/test.png")  # BGR, 0~255
    cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
    cv.imshow("input", image)
    index = 0
    while True:
        dst = cv.applyColorMap(image, colormap[index % 19])
        index += 1
        cv.imshow("color style", dst)
        c = cv.waitKey(400)
        if c == 27:
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    color_table_demo()

