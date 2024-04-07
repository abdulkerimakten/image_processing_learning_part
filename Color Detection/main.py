import cv2 as cv
from util import get_limits
## That method helps us to define a specific range for a decided color

from PIL import Image


# Color we want to detect
Color_to_detect = [0,0,255] # red in BGR code as example


# Set the camera (parameter depends on user's device)
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
        # turn the frame into numpy array
       
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            # coordinates of the box

            frame = cv.rectangle(frame, (x1,y1), (x2, y2), (0,255,0), 3)
        
        # ...CAMERA SECTION...
        cv.imshow("CAMERA", frame)

        # close the camera when 'q' is pressed.
        if cv.waitKey(40) & 0xFF == ord("q"):
            break


cap.release()
cv.destroyAllWindows()
