import cv2 as cv
import sys

"""
img_color = cv.imread("./study/image/test_gradation.jpg", cv.IMREAD_COLOR)
if img_color is None:
    print("파일을 읽을 수 없습니다.")
    sys.exit(1)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

cv.imshow('Grayscale', img_gray)
cv.imshow('Binary', img_binary)
cv.waitKey(0)
cv.destroyAllWindows()
"""

def on_trackbar(x):
    pass

img_color = cv.imread("./study/image/test_apple.jpg", cv.IMREAD_COLOR)
if img_color is None:
    print("파일을 읽을 수 없습니다.")
    sys.exit(1)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", img_gray)

cv.namedWindow("Binary")
cv.createTrackbar("threshold","Binary",0, 255, on_trackbar)
cv.setTrackbarPos("threshold","Binary",127)

while True:
    thresh = cv.getTrackbarPos("threshold","Binary")
    ret, img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY_INV)
    cv.imshow("Binary", img_binary)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()