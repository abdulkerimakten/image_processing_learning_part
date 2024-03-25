import cv2 as cv
import numpy as np


# Blank image
blank = np.zeros((500,500,3), dtype="uint8")

"""
Initializes a NumPy array representing an image with dimensions 500x500 pixels and 3 color channels (RGB).

"""

# # 1. Paint the image a certain colour.
# blank[:] = 0,255,0
# cv.imshow("Green Image", blank)
# cv.waitKey(0)


# # 2. red square
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Red Square", blank)
# cv.waitKey(0)


# # 3. Draw a blue rectangle
# cv.rectangle(blank, (0,0), (255,255), (255,0,0), thickness=3)
# cv.imshow("Blue Rectangle", blank)
# cv.waitKey(0)


# # 4. Draw a filled rectangle
# cv.rectangle(blank, (0,0), (255,400), (215,56,40), thickness=cv.FILLED) # or we can use "-1"
# cv.imshow("Color Filled  Rectangle", blank)
# cv.waitKey(0)


# # 5. Draw a Circle
# cv.circle(blank, (250,250), 40, (90,140,190), thickness=-1)
# cv.imshow("Color Filled  Circle", blank)
# cv.waitKey(0)


# # 6. Draw a Line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
# ## blank.shape[]... part means that "half part" of the "blank" window of image
# cv.imshow("Line", blank)
# cv.waitKey(0)


# 7. WRITING TEXT
cv.putText(blank, "HELLO WORLD", (20, 150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (1,255,1), thickness=2)
cv.imshow("MY TXT", blank)
cv.waitKey(0)