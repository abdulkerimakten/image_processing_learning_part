import cv2 as cv
import numpy as np

def get_limits(color):

    c = np.uint8([[color]]) # here insert the bgr values which you want to convert to hsv

    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    """"
    Define Lower and Upper Limits: The lower and upper limits for thresholding are defined 
    based on the HSV values of a specific pixel in the image. These values are typically determined empirically 
    based on the specific color range you want to detect.

    Lower Limit: It defines the lower bound of the color range you want to detect. The values (h - 10, 100, 100) 
    correspond to (Hue - 10, Saturation: 100, Value: 100). Here, h is the hue value of the pixel.

    Upper Limit: It defines the upper bound of the color range you want to detect. The values (h + 10, 255, 255) 
    correspond to (Hue + 10, Saturation: 255, Value: 255). Again, h is the hue value of the pixel.
    """

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit