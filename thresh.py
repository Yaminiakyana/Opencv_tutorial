import cv2 as cv
import numpy as np

img = cv.imread('hh.jpg')
cv.imshow('hh', img)
#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

#threshold inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

#adaptive thresholding
#it finds mean of the pixel values in the region of interest
#it then uses this mean to threshold the image
#it is used when the image has different lighting conditions
#it is used when the image has different intensity,contrast, brightness levels
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)   
cv.imshow('Adaptive Thresholding', adaptive_thresh)
cv.waitKey(0)