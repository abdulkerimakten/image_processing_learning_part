import cv2 as cv
from util import get_limits
from PIL import Image
import time

# Color we want to detect
Color_to_detect = [0, 0, 255]  # Red in BGR code as an example

# Set the camera (here we use the webcam)
cap = cv.VideoCapture(1)

# Initialize variables for FPS calculation
prev_time = 0
fps = 0

while True:

    # Read frames from the camera
    ret, frame = cap.read()

    if ret:

        # Making blur to enhance detection
        blur = cv.blur(frame, (3, 3))

        # Change the color spaces to define a color range
        hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Get the boundary values for the colour in HSV space
        lowerLimit, upperLimit = get_limits(color=Color_to_detect)

        # Set a mask to detect the color in frame
        mask = cv.inRange(hsv_img, lowerb=lowerLimit, upperb=upperLimit)

        # Bounding box part
        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            # Coordinates of the box

            frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
            # Define the text and position
            text = 'DETECTED'
            position = (x1 + 10, y2 + 30)  # Coordinates of the bottom-left corner of the text

            # Choose the font and other text properties
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_color = (0, 255, 255)  # Yellow color in BGR format
            thickness = 2  # Thickness of the text

            # Put the text on the image
            cv.putText(frame, text, position, font, font_scale, font_color, thickness)

        # Calculate FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        # Display FPS
        cv.putText(frame, f'FPS: {int(fps)}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Show the webcam feed
        cv.imshow("WEBCAM", frame)

        # Close the camera when 'q' is pressed.
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv.destroyAllWindows()
