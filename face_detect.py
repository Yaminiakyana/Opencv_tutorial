import cv2 as cv

img = cv.imread('group1.jpg')
cv.imshow('people', img)

#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
# scaleFactor: how much the image size is reduced at each image scale
# minNeighbors: how many neighboring rectangles must be detected to confirm a face
#if the number of faces detected is wrong then try to adjust the scaleFactor and minNeighbors
print(f'Number of faces found = {len(faces_rect)}')
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected Face', img)
cv.waitKey(0) 