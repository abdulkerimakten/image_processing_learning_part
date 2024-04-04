import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Original", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Adaptive Thresholding

"""METHOD
Unlike global thresholding, where a single threshold value is applied to the entire image, 
adaptive thresholding calculates the threshold for each pixel neighborhood separately, 
taking into account the local image characteristics.
"""

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 4)
cv.imshow("Adaptive Thresholed", adaptive_thresh)


"""
blockSize = '11' : Specifies the size of the pixel neighborhood used to calculate the adaptive threshold. 
This parameter determines the size of the area around each pixel that influences the threshold calculation.

C = '4': Represents a constant value subtracted from the calculated mean or weighted mean. 
It helps fine-tune the threshold value.
"""

cv.waitKey(0)
