import cv2

cap = cv2.VideoCapture("acha.MOV")

while True:
    success, img = cap.read()
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
