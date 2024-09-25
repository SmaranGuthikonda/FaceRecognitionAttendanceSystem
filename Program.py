import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import _datetime
import time
import csv


PATH = "/Users/smaran/Documents/Python_Programs/Final/Images"
imgs = []
image_file = os.listdir(PATH)
images = []
persons_names = []

ts = time.time()
dt = _datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
columns = ['Roll No', '', 'In Time']
path = "/Users/smaran/Documents/Python_Programs/Final/Attendance/"
fil = "Attendance"+dt+".csv"
with open(os.path.join(path, fil), 'w') as fp:
    pass

for img_file in image_file :
    img = cv2.imread(f"{PATH}/{img_file}")
    images.append(img)
    persons_name = img_file.split(".")[0]
    persons_names.append(persons_name)

def mark_attendance_list(name):
    with open("/Users/smaran/Documents/Python_Programs/Final/Attendance/"+fil, "r+") as f :
        current_list = f.readlines()

        names = []

        for item in current_list :
            entry = item.split(",")
            names.append(entry[0])

        if name not in names:
            cur_date = datetime.now()
            formatted_time = cur_date.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{formatted_time}")




def faceEncodings(img_list):
    encoding_list = []

    for image in img_list:
        encoding = face_recognition.face_encodings(image)[0]
        encoding_list.append(encoding)
        return encoding_list

known_encodings_list = faceEncodings(images)

cap = cv2.VideoCapture(0)

count = 0

while True:
    success, img = cap.read()

    if not success:
        break

    test_face_location = face_recognition.face_locations(img)
    test_encoded = face_recognition.face_encodings(img, test_face_location)
    
    for encoded_face, location in zip(test_encoded, test_face_location):
        matches = face_recognition.compare_faces(known_encodings_list, test_encoded[0])
        face_distances = face_recognition.face_distance(known_encodings_list,test_encoded[0])

        #print(face_distances)

        match_index = np.argmin(face_distances)

        if matches[match_index]:
            name = persons_names[match_index]

            y1, x2, y2, x1 = location
            
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 6)
            cv2.rectangle(img,(x1,y2-40),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
            
            mark_attendance_list(name)

        else : 
            na = "Unknown"
            name_date = datetime.now()
            name_time = name_date.strftime("%H:%M:%S")
            name = na + str(count)
            count += 1

            y1, x2, y2, x1 = location
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 6)
            cv2.rectangle(img,(x1,y2-40),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,"unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)

            

            if name == name :
                n = "Unknown"
                img_date = datetime.now()
                img_time = img_date.strftime("%H:%M:%S")
                str(img_time)
                img_path = "/Users/smaran/Documents/Python_Programs/Final/Anonymous/"
                img_fil = ".jpg"
                filename= img_path + name + img_time + img_fil
                cv2.imwrite(filename, img=img)
                img_ = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
                img_ = cv2.imshow("Unknow Face Detected", img_)
                print("Image saved!")
                mark_attendance_list(name)

    cv2.imshow("Facial Attendence",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
            print("Turning off camera.")
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


#cap.release()
