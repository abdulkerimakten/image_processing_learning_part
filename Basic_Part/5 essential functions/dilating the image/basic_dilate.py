import cv2 as cv

img = cv.imread("Photos/cat.jpg")
# cv.imshow("Normal Cat", img)

# canny_before_blur = cv.Canny(img, 125, 175)
# cv.imshow("CANNY EDGES BEFORE BLUR", canny_before_blur)


## First blur and then edge cascade

# show the blurred one
blurred = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("BLURRED IMAGE", blurred)

canny_after_blur = cv.Canny(blurred, 125, 175)
cv.imshow("CANNY EDGES AFTER BLUR", canny_after_blur)



# DILATING IMAGE
"""Dilation is a process of expanding or thickening the boundaries of objects in an image."""
"""Dilation is useful for tasks such as image segmentation, noise removal, and feature extraction."""

dilated = cv.dilate(canny_after_blur, (7,7), iterations=3)
cv.imshow("Dilated Image", dilated)



# ERODE Process
"""Erosion is a process of shrinking or thinning the boundaries of objects in an image."""
"""Erosion is useful for tasks such as separating touching objects, removing small objects, 
and preparing images for further processing."""

eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("ERODED", eroded)
# Here we get back the result before the dilating with the help of ERODE.


cv.waitKey(0)