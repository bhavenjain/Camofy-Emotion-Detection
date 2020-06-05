import cv2
import numpy as np

img = cv2.imread("cars.jpg")
cv2.imshow("Mask", img)
cv2.waitKey(0)

