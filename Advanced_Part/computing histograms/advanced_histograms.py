import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)


"""
## Grayscale Histogram

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# create a mask

blank = np.zeros(img.shape[:2], dtype="uint8")
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Mask", mask)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(gray_hist)
plt.xlim([0,256])

plt.show()

"""



## Color Histogram



# create a mask

blank = np.zeros(img.shape[:2], dtype="uint8")

circle_color = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask_color = cv.bitwise_and(img, img, mask=circle_color)
cv.imshow("Masked For Colored", mask_color)

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")

colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle_color, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)



""" FOR THE GRAY SCALE PART EXPLNTN
The result of these operations is a histogram of a grayscale image in the variable `gray_hist`. 
The histogram shows the intensity distribution of the pixels in the image. 
The histogram of a grayscale image shows the number of pixels of different grayscale levels (from 0 to 255) in the image.

For example, the values in `gray_hist` include the number of pixels in the image that have a value of 0 pixels, 
the number of pixels that have a value of 1 pixel, the number of pixels that have a value of 2 pixels, and so on to 255 pixels. 

This histogram can be used to analyze the brightness distribution and contrast of the image. 

The form of the histogram shows whether the image is light or dark, which grayscale levels are intense, 
and the distribution of pixel values. 

This information can be useful in image processing and analysis, for example in applications 
such as image segmentation, edge detection, brightness correction and histogram equalization.
"""