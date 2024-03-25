import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Simple Thresholding

## Normal Binarization
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded", thresh)


## Inverse Binarization
threshold, thresh_inverse = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded Inverse", thresh_inverse)



cv.waitKey(0)