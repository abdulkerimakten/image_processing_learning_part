import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Original Image Cats", img)

# Translation (shifting)

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
"""
In OpenCV, 
warpAffine() function expects the output image dimensions to be in the format (width, height) rather than (height, width). 
This convention is consistent across many image processing libraries and functions.
"""

# -x ==> left
# -y ==> up
# x ==> right
# y ==> down

translated = translate(img, 100, -100)
cv.imshow("TRANSLATED", translated)

cv.waitKey(0)