import cv2 as cv

## Path to webcam
webcam = cv.VideoCapture(0)
# Generally "0" for webcam of device


## Reading Frames from Webcam
while True:

    ret, frame = webcam.read()

    cv.imshow("Webcam", frame)

    if cv.waitKey(40) & 0xFF == ord("q"):
        break
    # To close the camera we define this condition.

webcam.release()
cv.destroyAllWindows()