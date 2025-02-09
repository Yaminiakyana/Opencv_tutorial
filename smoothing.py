import numpy as np
import cv2 as cv

img = cv.imread('hh.jpg')
cv.imshow('hh', img)

#Average
average = cv.blur(img, (3,3))
cv.imshow('Average blur', average)

# Gaussian Blur
# this is less blurer than average blur 
gb = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian blur', gb)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# Bilateral
# this is the best blur method
# it is used to remove the noise from the image
bilateral = cv.bilateralFilter(img, 3, 50, 50)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)