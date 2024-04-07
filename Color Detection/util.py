import numpy as np
import cv2


def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

    """"
    Define Lower and Upper Limits: The lower and upper limits for thresholding are defined 
    based on the HSV values of a specific pixel in the image. These values are typically determined empirically 
    based on the specific color range you want to detect.

    Lower Limit: It defines the lower bound of the color range you want to detect. The values (h - 10, 100, 100) 
    correspond to (Hue - 10, Saturation: 100, Value: 100). Here, h is the hue value of the pixel.

    Upper Limit: It defines the upper bound of the color range you want to detect. The values (h + 10, 255, 255) 
    correspond to (Hue + 10, Saturation: 255, Value: 255). Again, h is the hue value of the pixel.
    """
