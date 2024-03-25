import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Laplacian

with_laplace = cv.Laplacian(gray, cv.CV_64F)
with_laplace = np.uint8(np.absolute(with_laplace))
cv.imshow("Laplacian", with_laplace)

"""
The cv.Laplacian() function returns a floating-point data type array, which represents the gradient image. 
However, to display the gradient image using cv.imshow(), the pixel values need to be converted 
back to the appropriate data type for displaying images (typically unsigned 8-bit integers, uint8).


np.absolute(with_laplace): This part computes the absolute value of each pixel in the Laplacian gradient image. 
The Laplacian operation can produce both positive and negative values, depending on the rate of change of pixel intensities. 
Taking the absolute value ensures that all pixel values are positive.

np.uint8(): This part converts the array resulting from the absolute operation to the uint8 data type,
which is suitable for image display using cv.imshow(). The uint8 data type represents pixel values in the range [0, 255].

"""

cv.waitKey(0)