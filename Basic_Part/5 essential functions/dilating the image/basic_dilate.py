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

"""
'kernel = (7, 7)' : This parameter defines the structuring element used for dilation. It's a 7x7 square-shaped structuring element, 
indicating the neighborhood around each pixel that is considered during the dilation operation.

'iterations=3' : This parameter specifies the number of times dilation is applied. In this case, dilation will be applied three times, 
which increases the effect of expanding the boundaries of foreground objects.

The function performs dilation by moving the structuring element over the input image. 
At each position, if at least one pixel under the structuring element is white (255), the output pixel is set to white; otherwise, it remains black (0). 
This process effectively expands the boundaries of foreground objects, making them larger.
"""

cv.imshow("Dilated Image", dilated)



# ERODE Process
"""Erosion is a process of shrinking or thinning the boundaries of objects in an image."""
"""Erosion is useful for tasks such as separating touching objects, removing small objects, 
and preparing images for further processing."""

eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("ERODED", eroded)
# Here we get back the result before the dilating with the help of ERODE.


cv.waitKey(0)
