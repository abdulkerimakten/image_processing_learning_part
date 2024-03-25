import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("ORIGINAL", img)



### split part...
b,g,r = cv.split(img)


# cv.imshow("Blue Parts", b)
# Blue parts will be more white
# cv.imshow("Green Parts", g)
# Green parts will be more white
# cv.imshow("Red Parts", r)
# Red parts will be more white




### merge part...
merge = cv.merge([b,g,r])
cv.imshow("Merged Image", merge)



#######################################################################################################################


### showing the image in one special color channel

## First we create a blank on which each color channel will be displayed

blank = np.zeros(img.shape[:2], dtype="uint8")

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue Painted", blue)
cv.imshow("Green Painted", green)
cv.imshow("Red Painted", red)

cv.waitKey(0)