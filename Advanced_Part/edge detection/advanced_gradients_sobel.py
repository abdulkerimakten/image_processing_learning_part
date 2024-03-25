import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
# cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)



# Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)
cv.imshow("Sobel Combined", sobel_combined)

# comparing with canny edges
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny Edges", canny)


cv.waitKey(0)