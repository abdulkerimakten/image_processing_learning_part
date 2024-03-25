import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
# cv.imshow("Original Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
"""
Pixels with intensity values greater than 125 are set to 255 in the output image (thresh),
and pixels with intensity values less than or equal to 125 are set to 0.
"""
cv.imshow("Thresh", thresh)



#finding contours using threshold
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found.')




## drawing contours on a blank

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

cv.drawContours(blank, contours, -1, (0,255,0), 1)
"""contourIdx: Index of the contour to draw. If -1 is specified, all contours are drawn."""
cv.imshow("Contours Drawn on Blank", blank)



cv.waitKey(0)