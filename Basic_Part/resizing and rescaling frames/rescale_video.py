import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3,width)
    capture.set(4,height)

"""
frame ---> It represents the image whose dimensions need to be changed.
dimensions ---> It's a tuple specifying the new dimensions (width, height) of the image.

interpolation=cv.INTER_AREA ---> This parameter specifies the interpolation method to be used during the resizing operation. 
In this code, cv.INTER_AREA is used, which stands for Area-Based Interpolation. 
This method is suitable for shrinking images and provides better results for downsizing operations.
"""


if __name__ == "__main__":
    # Reading Videos

    pathway_to_media = "D:/Image_Processing_Section/FreeCodeAcademy/Basic_Part/Videos/dog.mp4"

    capture = cv.VideoCapture(pathway_to_media)

    while True:

        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame,scale=.2) # more smaller that is resized as multiplied by 0.2

        

        cv.imshow("Original Video", frame) # Original one that is more large window
            
        cv.imshow("Resized Video", frame_resized) # Rescaled one that is more narrow window

        if cv.waitKey(20) & 0xFF == ord("d"):
            break

        """
        This ord() function converts the character "a" to its corresponding Unicode keycode, 
        and then it can be compared with the keycode returned by cv.waitKey().
        """

    capture.release()
    cv.destroyAllWindows()