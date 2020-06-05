import cv2
import numpy as np

img = cv2.imread("road.jpg")
kernal = np.ones((2,2), np.uint8)     #uint ---> unsigned integer

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 150, 200)             # drawing
imgDilation = cv2.dilate(imgCanny, kernal, iterations=1)
imgEroded = cv2.erode(imgDilation, kernal, iterations=1)

cv2.imshow("Output", img)
cv2.imshow("Gray Output", imgGray)
cv2.imshow("Blur Output", imgBlur)
cv2.imshow("Canny Output", imgCanny)
cv2.imshow("Dilation Output", imgDilation)
cv2.imshow("Eroded Output", imgEroded)

cv2.waitKey(0)