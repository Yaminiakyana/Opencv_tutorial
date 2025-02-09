import cv2 as cv
import numpy as np

img = cv.imread('hh.jpg')
cv.imshow('hh', img)
# masking
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv.rectangle(mask, (30, 30), (300, 200), 255, -1)
cv.imshow('Mask', mask)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked)
cv.waitKey(0)