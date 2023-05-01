import os
import cv2
import uuid
import time

labels = ['thumpsup', 'thumsdown', 'thankyou', 'mobile']
num_img = 20
IMG_PATH = r"Tensorflow\Workspace\images\collectedimages"
if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)
for label in labels:
    if not os.path.exists(os.path.join(IMG_PATH, label)):
        os.makedirs(os.path.join(IMG_PATH, label))

cap = cv2.VideoCapture(0)
for label in labels:
    print(f"Collecting {label}")
    time.sleep(5)
    for i in range(num_img):
        _, frame = cap.read()
        cv2.imwrite(os.path.join(IMG_PATH, label, str(uuid.uuid1())+'.jpg'), frame)
        cv2.imshow('Capture', frame)
        time.sleep(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()
    