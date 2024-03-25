import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow("Original", img)



"""Differences btween 2 libraries (Matplot / OpenCV)
## Here our image will be shown in a format "RGB" inverse of Opencv
plt.imshow(img)
plt.show()

## Solution for this
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB Version", rgb)

plt.imshow(rgb)
plt.show()

"""

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)




# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Color", hsv)






# BGR to LAB(L*a*b)

# L = lightness
# a = green to magenta
# b = blue to yellow

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB color", lab)



# Inverse Operation...


# HSV to BGR

hsv_to_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_to_bgr)


cv.waitKey(0)
