import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Normal Cat", img)

canny_before_blur = cv.Canny(img, 125, 175)
cv.imshow("CANNY EDGES BEFORE BLUR", canny_before_blur)
"""
threshold1 = '125': Specifies the lower threshold value for edge detection. Gradient values below this threshold are suppressed and considered as non-edges.

threshold2 = '175': Specifies the upper threshold value for edge detection. Gradient values above this threshold are considered as strong edges, 
while gradient values between the lower and upper thresholds are considered as weak edges.
"""

## First blur and then edge cascade

# show the blurred one
blurred = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("BLURRED IMAGE", blurred)

canny_after_blur = cv.Canny(blurred, 125, 175)
cv.imshow("CANNY EDGES AFTER BLUR", canny_after_blur)

cv.waitKey(0)


