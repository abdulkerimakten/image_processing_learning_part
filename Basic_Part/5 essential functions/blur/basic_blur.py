import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Normal Image", img)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("BLURRED IMAGE", blur)


cv.waitKey(0)