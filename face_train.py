#pylint:disable=no-member
import os
import cv2 as cv
import numpy as np

people = ['Ian', 'Jl', 'Tom']
DIR = '/Users/akyanayamini/Documents/AIML/opencv/Faces'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        if not os.path.exists(path):
            print(f"Error: Directory {path} does not exist.")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Error: Image {img_path} not found or unable to load.")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = cv.resize(gray[y:y+h, x:x+w], (200, 200))
                features.append(faces_roi)
                labels.append(label)

create_train()
print(f"Training done — Number of features: {len(features)}, Number of labels: {len(labels)}")

# Create the recognizer and train it
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, np.array(labels))
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)
print("Model saved successfully.")