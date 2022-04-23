import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
img = cv2.imread('download1.jpg')
faces = face_cascade.detectMultiScale(img,1.1,4)
#making rectangle
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('faces detected.jpg', img)
cv2.waitKey()