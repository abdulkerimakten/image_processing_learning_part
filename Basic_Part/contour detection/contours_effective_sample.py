import cv2 as cv

# Read image
img = cv.imread("Photos/real_birds.jpg")

img_copy = cv.imread("Photos/real_birds.jpg")

# Grayscale Image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Thresholding on the grayscaled image
ret, thresh = cv.threshold(img_gray, 125, 255, cv.THRESH_BINARY_INV)

""""
Pixels with intensity values greater than 125 are set to 255 in the output image (thresh),
and pixels with intensity values less than or equal to 125 are set to 0.
"""

# Finding Contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    print(cv.contourArea(cnt))
    if cv.contourArea(cnt) > 200:
        ## Drawing Boundaries
        # cv.drawContours(img_copy, cnt, -1,(0,255,0), 1)
        # this method add green borders around the detected objects founded with the help of contours
        """contourIdx: Index of the contour to draw. If -1 is specified, all contours are drawn."""
        


        ## Drawing Rectangles around objects detected
        x, y, w, h = cv.boundingRect(cnt)
        """if you have a contour cnt representing an object in an image, 
        using cv.boundingRect(cnt) will give you the smallest rectangle that completely encloses that object in given color. """
        cv.rectangle(img_copy, (x,y), (x+w, y+h), (0,255,0), 2)


cv.imshow("ORIGINAL", img)
# cv.imshow("Gray", img_gray)
# cv.imshow("Thresh", thresh)
cv.imshow("CONTOURS", img_copy)

cv.waitKey(0)