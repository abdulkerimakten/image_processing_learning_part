import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Normal Cat", img)

canny_before_blur = cv.Canny(img, 125, 175)
cv.imshow("CANNY EDGES BEFORE BLUR", canny_before_blur)


## First blur and then edge cascade

# show the blurred one
blurred = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("BLURRED IMAGE", blurred)

canny_after_blur = cv.Canny(blurred, 125, 175)
cv.imshow("CANNY EDGES AFTER BLUR", canny_after_blur)

cv.waitKey(0)


