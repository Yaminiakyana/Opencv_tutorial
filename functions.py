import cv2 as cv

img = cv.imread('horse1.jpg')
cv.imshow('Horse',img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge cascade
#you can also use the blur image to get the edges
#but the blur image have less edges
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges',canny)

#Dilating the image
#it is used to increase the thickness of the edges
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated',dilated)

#Eroding
#it is used to decrease the thickness of the edges
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded',eroded)

#Resize
resize = cv.resize(img , (500,500), interpolation = cv.INTER_AREA)
cv.imshow('Resized',resize)

#Cropping
cropped = img[100:200, 200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)