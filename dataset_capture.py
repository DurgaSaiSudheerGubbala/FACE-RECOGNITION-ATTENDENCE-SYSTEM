# Import OpenCV2 for image processing
import csv
import cv2
import os

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

    
face_id=input('enter your id')
name = input("Enter Your Name: ")

if(is_number(face_id) and name.isalpha()):
    # Start capturing video
    vid_cam = cv2.VideoCapture(0)
    # Detect object in video stream using Haarcascade Frontal Face
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Initialize sample face image
    count = 0
    assure_path_exists("dataset/")
    # Start looping
    while(True):
        # Capture video frame
        _, image_frame = vid_cam.read()
        # Convert frame to grayscale
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        # Detect frames of different sizes, list of faces rectangles
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        # Loops for each faces
        for (x,y,w,h) in faces:
            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            # Increment sample face image
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/" + name + '.' + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            # Display the video frame, with bounded rectangle on the person's face
            cv2.imshow('frame', image_frame)
            # To stop taking video, press 'q' for at least 100ms
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # If image taken reach 100, stop taking video
        elif count>=30:
            print("Successfully Captured")
            break
        # Stop video
    vid_cam.release()
    # Close all started windows
    cv2.destroyAllWindows()
    res = "Images Saved for ID : " + face_id + " Name : " + name
    row = [face_id, name]
    with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
else:
    if(is_number(face_id)):
        print("Enter Alphabetical Name")
    if(name.isalpha()):
        print("Enter Numeric ID")
   
