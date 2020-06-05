import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

#print(img)

#to convert the whole image to colour blue
#img[:] = 255,0,0

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)     #height, width
cv2.rectangle(img, (0,0), (250,350), (0,0,255) , 1)                 # 1 is the thickness
#to fill the rectangle
#cv2.rectangle(img, (0,0), (250,350), (0,0,255) , cv2.FILLED)

cv2.circle(img, (400,50), 30, (255,255,0) , 2)

cv2.putText(img, "  OPENCV  ",(300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 2)

cv2.imshow("Output", img)
cv2.waitKey(0)