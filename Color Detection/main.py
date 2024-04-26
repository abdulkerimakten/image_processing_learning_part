import cv2 as cv
from util import get_limits
## That method helps us to define a specific range for a decided color

from PIL import Image


# Color we want to detect
Color_to_detect = [0,255,255] # red in BGR code as example


# Set the camera (choose whatever you want)
cap = cv.VideoCapture(1)

while True:

    # read frames from camera
    ret, frame = cap.read()

    if ret:
        
        # Making blur to enhance detection
        blur = cv.blur(frame, (3,3))

        ## Change the color spaces to define a color range
        hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Get the boundary values for the colour in HSV space
        lowerLimit, upperLimit = get_limits(color=Color_to_detect)
        
        # set a mask to detect the color in frame
        mask = cv.inRange(hsv_img, lowerb=lowerLimit, upperb=upperLimit)

        


        ## Bounding box part
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            # coordinates of the box

            frame = cv.rectangle(frame, (x1,y1), (x2, y2), (0,255,0), 3)
            # Define the text and position
            text = 'DETECTED'
            position = (x1+10, y2 + 30)  # Coordinates of the bottom-left corner of the text

            # Choose the font and other text properties
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_color = (0, 255, 255)  # White color in BGR format
            thickness = 2  # Thickness of the text

            # Put the text on the image
            cv.putText(frame, text, position, font, font_scale, font_color, thickness)
        
        # ...CAMERA SECTION...
        cv.imshow("WEBCAM", frame)

        # close the camera when 'q' is pressed.
        if cv.waitKey(40) & 0xFF == ord("q"):
            break


cap.release()
cv.destroyAllWindows()
