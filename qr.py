import cv2
import numpy as np
from pyzbar import pyzbar

cap= cv2.VideoCapture(0)
font= cv2.FONT_HERSHEY_PLAIN

while cap.isOpened():   #always return true value
    ret,frame= cap.read()
    
    decodeObjects= pyzbar.decode(frame)
    
    for obj in decodeObjects:
        #print("Data", obj.data)
        
        cv2.putText(frame, str(obj.data), (50,50), font, 2, (255,0,0), 2)
    
    if ret==True:    
        frame= cv2.resize(frame, (720, 450))
        grey= cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
        cv2.imshow("frame", frame)
        cv2.imshow("grey",grey)
        k= cv2.waitKey(1)
        if k==ord("z") & 0xFF:
            break

cap.release()
cv2.destroyAllWindows()