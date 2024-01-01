import cv2 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # we don't have this 

img = cv2.imread('test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRAY)

faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)

cv2.imshow()
cv2.waitKey()

cv2.imwrite("Face_Detected.jpg", img)