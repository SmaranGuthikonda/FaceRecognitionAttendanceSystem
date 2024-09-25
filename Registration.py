import face_recognition
import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

'''while True :
     
     _, img = cap.read()
     picture_of_me = face_recognition.load_image_file("/Users/smaran/Documents/Python_Programs/Final/Images/B20CS127.jpg")
     my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
     # my_face_encoding now contains a universal 'encoding' of my facial features that can˓→be compared to any other picture of a face!
     unknown_picture = face_recognition.load_image_file("/Users/smaran/Documents/Python_Programs/Final/Images/B20CS121.jpg")
     unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
     # Now we can see the two face encodings are of the same person with `compare_faces`! 
     results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
     
     if results[0] == True:
         print("It's a picture of me!")
     else:
         print("It's not a picture of me!")
         '''

count = 0

Roll_No = str(input("Enter Your Roll No : ")).upper()

directory = Roll_No
parent_dir = "/Users/smaran/Documents/Python_Programs/Final/Images"
#path = os.path.join(parent_dir, directory)
#os.mkdir(path)

if os.path.exists(parent_dir) :
    os.chdir(parent_dir)
else :
    os.mkdir(parent_dir)
    os.chdir(parent_dir)

while True:
    try : 
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame,1.3,5)
        cv2.imshow(" Registration ",frame)
        key = cv2.waitKey(1)

        if key == ord('s'):
            for x,y,w,h in faces :
                count = count+1
                name = Roll_No + '.jpg'
                print("Creating images .....",name)
                os.chdir(parent_dir)
                cv2.imwrite(name, img=frame)
                img_ = cv2.imread(name, cv2.IMREAD_ANYCOLOR)
            #cv2.imwrite(name,frame[y:y+h,x:x+w])
            # #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            if count > 0 :
                break

        elif key == ord('q'):
            cv2.imshow(" Turning off camera ",frame)
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    except(KeyboardInterrupt):
        cv2.imshow(" Turning off camera ",frame)
        cap.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

