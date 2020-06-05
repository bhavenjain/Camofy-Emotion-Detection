import cv2
import numpy as np

img = cv2.imread("cards.jpg")

width,height = 250,350
pst1 = np.float32([[269,82], [469,82], [306,309], [535,305]])
pst2 = np.float32([[0,0], [width,0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pst1, pst2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", imgOutput)
cv2.waitKey(0)