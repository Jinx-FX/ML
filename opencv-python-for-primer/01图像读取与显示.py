import cv2 as cv

image = cv.imread("test/test.png")
cv.imshow("input", image)
cv.waitKey(0)
cv.destroyAllWindows()

