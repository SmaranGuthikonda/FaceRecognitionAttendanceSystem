import cv2
import face_recognition

img27 = cv2.imread("/Users/smaran/Documents/Python_Programs/Final/Images/B20CS127.jpg")
test_img = cv2.imread("/Users/smaran/Documents/Python_Programs/Final/Images/B20CS121.jpg")

face_location = face_recognition.face_locations(img27)[0]
test_face_location = face_recognition.face_locations(test_img)[0]

cv2.rectangle(img27,(face_location[3],face_location[0]),(face_location[1],face_location[2]),(255,255,0),3)
cv2.rectangle(test_img,(face_location[3],face_location[0]),(face_location[1],face_location[2]),(255,255,0),3)

encodedimg27 = face_recognition.face_encodings(img27)[0]
encodedtestimg = face_recognition.face_encodings(test_img)[0]
#print(encodedimg27)

comparison_result = face_recognition.compare_faces([encodedimg27],encodedtestimg)
print(comparison_result)

faces_distances = face_recognition.face_distance([encodedimg27],encodedtestimg)
print(faces_distances)



cv2.imshow("B20CS127",img27)
cv2.imshow("B20CS121",test_img)

cv2.waitKey(1000)
