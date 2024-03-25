import cv2 as cv
from rescale_video import rescaleFrame

pathway_to_media = "D:/Image_Processing_Section/FreeCodeAcademy/Basic_Part/Photos/cat.jpg"

img = cv.imread(pathway_to_media)
img_resized = rescaleFrame(img, .5) # as rate of 0.5

cv.imshow("Resized Cat Image", img_resized)
cv.imshow("Orginal Cat Image", img)

cv.waitKey(0)

