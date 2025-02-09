import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('hh.jpg')
cv.imshow('Horse',img)

plt.imshow(img)
plt.show()
# # gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# # BGR to HSV
# # HSV is used to detect the color of the object
# # HSV = Hue Saturation Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# # BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv. waitKey(0)