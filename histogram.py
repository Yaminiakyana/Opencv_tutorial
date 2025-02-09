import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('hh.jpg')
cv.imshow('hh', img)
#gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

#blank
blank = np.zeros(img.shape[:2], dtype='uint8')

#circle
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

#mask
mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)
#histogram
# blank = np.zeros(img.shape[:2], dtype='uint8')
# gray_hist = cv.calcHist([gray], [0], circle, [256], [0, 256])
# cv.imshow('gray_hist', gray_hist)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('bins')
plt.ylabel('no of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()
#color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
    plt.title('Color Histogram')
plt.show()
cv.waitKey(0)