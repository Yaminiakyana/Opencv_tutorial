import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500,500,3),dtype='uint8')
# uint8 is the data type of the image
# cv.imshow('Blank',blank)
# # Here the 200 and 300 are the pixels of the image
# # blank[200:300, 300:400] = 255,0,0
# # cv.imshow('Blue',blank)

# # Draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,250,0), thickness=2)

# # Draw a filled rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,250,0), thickness=cv.FILLED)
# cv.imshow('rectangle', blank)

#Write text
cv.putText(blank,'Hello,my name is Munny',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)