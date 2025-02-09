import cv2 as cv
import numpy as np

img = cv.imread('hh.jpg')
cv.imshow('Horse',img)

#blank
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)
 # Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#there is another way to find the countours
#Apply threshold
#it is used to convert the image into binary image
#it is used to remove the noise from the image
ret , thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

# #Blur
# #it is used to remove the noise from the image
# blur = cv.GaussianBlur(gray, (5,5), 0)
# cv.imshow('Blur', blur)
# #Edge cascade
# edges = cv.Canny(blur, 50, 150)
# cv.imshow('Edges', edges)

#Contours
#Contours are the boundaries of the object
#Contours are used to detect the object in the image
#Contours are used to detect the shape of the object in the image


#you can decrease the no of countours by making the image as blur
#and then pass the blur image to the canny function
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

#Draw the contours
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
