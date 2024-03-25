import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
# this blank will be our template for the mask so it needs to have same size as image 

circle_mask = cv.circle(blank, (img.shape[1]//2 + 10, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle Mask", circle_mask)



masked_image = cv.bitwise_and(img, img, mask=circle_mask)
cv.imshow("Masked Image", masked_image)


cv.waitKey(0)