import cv2 as cv

img = cv.imread("Photos/cat.jpg")

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
"""
In OpenCV, the interpolation parameter of the cv.resize() function specifies the method to be used for this filling process. 
For example, the cv.INTER_CUBIC parameter indicates the use of cubic interpolation. 
This method takes a weighted average of surrounding pixels to calculate the value of each new pixel, resulting in a smoother image.
"""
cv.imshow("Resized", resized)



# Crop
cropped = img[50:200, 200:400]
cv.imshow("CROPPED", cropped)

cv.waitKey(0)