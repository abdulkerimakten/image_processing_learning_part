import cv2 as cv

# img = cv.imread("Photos/cat.jpg")

# cv.imshow("CAT", img)

# cv.waitKey(0)

#---------------------------------------------------------------------------------

# Reading Videos (For dog video)

capture = cv.VideoCapture("Videos/dog.mp4")

while True:

    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow("Video", frame)
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    else:
        break

    """
    This ord() function converts the character "a" to its corresponding Unicode keycode, 
    and then it can be compared with the keycode returned by cv.waitKey().
    """

capture.release()
cv.destroyAllWindows()

"""
isTrue, frame = capture.read(): The capture.read() method reads the next frame and assigns it to the variable 'frame'.
isTrue is a boolean value indicating whether the frame was successfully read. If isTrue is False, it means the end of the video file is reached, and the loop exits.

cv.imshow("Video Of Dog", frame): The cv.imshow() method is used to display an image in a window.
This line creates a window named 'Video Of Dog' and displays the frame in the 'frame' variable in this window.

if cv.waitKey(20) & 0xFF == ord('d'): This line checks if a key is pressed. The cv.waitKey(20) method waits for a key to be pressed for 20 milliseconds 
after each frame. If the user presses the 'd' key (0xFF == ord('d')), the loop exits.

capture.release(): Releases the VideoCapture object. This is important to release resources when we've finished processing the video file.

cv.destroyAllWindows(): Closes all OpenCV windows. This ensures all windows are closed when we terminate the program.
"""



### Reading Video (for kitten video)

video = cv.VideoCapture(r"Videos\kitten.mp4")

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv.imshow("Kitten", frame)
        cv.waitKey(40)

# NOTE: While making condition this is more sensible.

video.release()
cv.destroyAllWindows()


