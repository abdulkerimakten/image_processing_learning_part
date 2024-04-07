import os
import cv2 as cv
import argparse
import mediapipe as mp




# ------------------ CREATION OF ANONYMIZER  ------------------ #

## Set this face anonymizer process as 'single process method'
def process_image(img, face_detection):
    # set the relative bounding box sizes to real dimensions of the face
    H, W, _ = img.shape
    
    # mediapipe works with images in RGB format
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

     # we need to feed the model with the images that absolutely contain real faces
    output = face_detection.process(img_rgb)

    if output.detections is not None:
        for detection in output.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x, y, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x = int(x*W)
            y = int(y*H)
            w = int(w*W)
            h = int(h*H)

            # img = cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 5)
            # we don't need to draw rectangle anymore



            ## Blur faces
            # we need to adjust the area of the face that we will blur
            img[y: y+h, x: x+w, :] = cv.blur(img[y: y+h, x: x+w, :], (70,70))
    
    return img




"""The mission of the argparse module is to facilitate the creation of command-line interfaces in Python programs 
by parsing command-line arguments and options, handling errors, and defining a specific command-line interface structure. 
It aims to simplify the process of building flexible and user-friendly command-line programs."""

args = argparse.ArgumentParser()
args.add_argument("--mode")
args.add_argument("--file_path")
args = args.parse_args()


# Destination to save the output of the process
output_dir = r"Out_of_face_anonymizer"


## Detect faces using "mediapipe" library
mp_face_detection = mp.solutions.face_detection





        #------------------------ FACE DETECTION PART -------------------#

# Creating "face detection" tool to use
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    
    # >Choose any mode you want <
    # args.mode = "image"
    # args.mode = "video"
    args.mode = "webcam"

    if args.mode in ["image"]:
        
        ## Read Image
        args.file_path = r"Photos\lady.jpg" # this part is optional. You can cary the path
        img = cv.imread(args.file_path)
        img = process_image(img, face_detection)


        # Save Image
        cv.imwrite(os.path.join(output_dir, "output.jpg"), img)


    elif args.mode in ["video"]:
        
        ## Read Frames
        args.file_path = r"Videos\boy.mp4"



        """
        This line of code creates a VideoCapture object named cap using the cv.VideoCapture() function from the OpenCV library. 
        It initializes a video capture from a specified file path, which is provided as an argument args.file_path. 
        This allows the program to read frames from the specified video file for further processing."""
        cap = cv.VideoCapture(args.file_path)
        
        ret, frame = cap.read()

        # Object created for saving the processed video in a specific location
        Output_video = cv.VideoWriter(os.path.join(output_dir, "output.mp4"), cv.VideoWriter.fourcc(*'MP4v'),
                                      25, (frame.shape[1], frame.shape[0]))
        
        """
        The first argument is the output file path where the video will be saved. 
        It uses os.path.join() to concatenate the output_dir (output directory) and the file name "output.mp4".
        
        The second argument is the four-character code representing the codec used for encoding the video. 
        In this case, it's specified as 'MP4v', which corresponds to the MPEG-4 Video codec.
        
        The third argument is the frame rate of the output video. Here, it's set to 25 frames per second.
        The fourth argument is a tuple representing the width and height of the video frame. 
        It's specified as (frame.shape[1], frame.shape[0]), which corresponds to the width and height of the input frame. 
        This ensures that the output video will have the same dimensions as the input frames.
        """

        while ret:
            
            # process the retrieved frame
            frame = process_image(frame, face_detection=face_detection)
            
            # Save the processed frame
            Output_video.write(frame)

            # Read new frames
            ret, frame = cap.read()


        # This is important to free up system resources 
        cap.release()
        Output_video.release()
    
    elif args.mode in ["webcam"]:

        # Capture the camer whichever you want to use
        cap = cv.VideoCapture(0)

        # Retrieve the frames from camera
        ret ,frame = cap.read()

        while ret:
            
            frame = process_image(frame, face_detection=face_detection)

            # Display the processed views  
            cv.imshow("BLURRED", frame)
            
            
            if cv.waitKey(25) & 0xFF == ord('q'):
                break

            ret, frame = cap.read()

        cap.release()