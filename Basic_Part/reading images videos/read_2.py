import cv2 as cv
import time

capture = cv.VideoCapture("Videos/dog.mp4")

start_time = None

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video Of Dog", frame)

    key = cv.waitKey(20)

    if key == ord("d"):
        start_time = time.time()  # save the starte time when "d" pressed

        # counting after the press "d"

        while time.time() - start_time < 2:
            if cv.waitKey(1) & 0xFF == ord("d"):
                break
            # here video stops

        # after reaching 2 seconds break the video
        if time.time() - start_time >= 2:
            break

capture.release()
cv.destroyAllWindows()
current_time = time.time()
print(current_time-start_time)
