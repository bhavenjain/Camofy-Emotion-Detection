import cv2
import numpy as np

img = cv2.imread("road.jpg")
imgResize = cv2.resize(img, (720,400))     # width, height
print(img.shape)
print(imgResize.shape)

imgCrop = img[0:900, 100:1200]         # height, width
print(imgCrop.shape)


#cv2.imshow("Output", img)
cv2.imshow("Resize Output", imgResize)
cv2.imshow("Crop Output", imgCrop)

cv2.waitKey(0)
