import cv2

img = cv2.imread("crop.jpg")

cv2.imshow("output", img)
cv2.waitKey(0)