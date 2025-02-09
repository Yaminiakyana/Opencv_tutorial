import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ian', 'Jl']
#features = np.load('features.npy', allow_pickle=TRUE)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml') 

img = cv.imread(r'/Users/akyanayamini/Documents/AIML/opencv/Faces/Ian/ian13.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)
#detect the face in the image
#the directory should contain atleast 10-20 images then you can get confidence score.
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]}, Confidence = {confidence}')
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)