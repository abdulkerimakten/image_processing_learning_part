import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Normal Image", img)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("BLURRED IMAGE", blur)


"""
'(3,3)': Specifies the kernel size. Gaussian blur employs a weighted averaging operation based on a Gaussian distribution. 
Hence, this parameter specifies the size of the Gaussian kernel. Here, using (3,3) creates a 3x3 Gaussian kernel.

'cv.BORDER_DEFAULT': This parameter denotes how borders will be handled. In this case, it represents using the default border pixel values.
"""
cv.waitKey(0)
