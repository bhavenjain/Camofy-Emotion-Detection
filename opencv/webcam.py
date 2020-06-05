import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 640)     # 3 id for width
cap.set(4, 480)     # 4 id for height
cap.set(10, 100)    # 10 id for brightness

while True:
    success, img = cap.read()
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):       #press q to exit
        break
