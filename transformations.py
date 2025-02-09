import cv2 as cv
import numpy as np

img = cv.imread('horse1.jpg')
cv.imshow('Horse',img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> move left
#-y --> move up
# x --> move right
# y --> move down
# image moved 100 pixels right and 100 pixels down
# translated = translate(img, 100, 100)
# image moved 100 pixels left and 100 pixels down
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (h, w) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (w//2, h//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (w,h)
    return cv.warpAffine(img, rotMat, dimensions)
# positive angle --> anti-clockwise rotation
# negative angle --> clockwise rotation
# rotated = rotate(img, 45)
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated Rotated', rotated_rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
# 0 --> flip vertically
# 1 --> flip horizontally
flipped = cv.flip(img, 1)
cv.imshow('Flipped', flipped)
cv.waitKey(0)
