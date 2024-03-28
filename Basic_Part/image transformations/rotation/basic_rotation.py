import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Original Image Cats", img)

"""
def rotate(img, angle, rotatePoint = None):
    (height, width) = img.shape[:2]
    
    if rotatePoint == None:
        rotatePoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotatePoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow("Rotated Image", rotated)

## We can also rotate the rotated image
rotated_rotated = rotate(rotated, 45)
cv.imshow("Rotated the Rotated Image", rotated_rotated)
## there will be some black triangles coming from first rotated one


## We can see originally how the img can be rotated by 90 degree clockwisely

rotated_by_90 = rotate(img, -90)
cv.imshow("ROTATING ORIGINAL by 90", rotated_by_90)

"""


# Resizing

# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
# The tuple (500, 500) represents (width, height) in the context of resizing the image.
# cv.imshow("RESIZED", resized)
"""
- If you are shrinking use : default or ..._AREA
- If you are enlarging use : ..._LINEAR or ..._CUBIC
"""



# Flipping 
flipped = cv.flip(img, 1)
cv.imshow("Flipped", flipped)
# 0 >> vertically
# 1 >> horizontally
# -1 >> both vertically and horizontally

cv.waitKey(0)
