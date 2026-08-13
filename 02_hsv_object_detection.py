import cv2,numpy as np
cap=cv2.VideoCapture(0)
while True:
    ok,f=cap.read()
    if not ok: break
    hsv=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,np.array([35,70,50]),np.array([85,255,255]))
    cs,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in cs:
        if cv2.contourArea(c)>500:
            x,y,w,h=cv2.boundingRect(c); cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Object Detection",f)
    if cv2.waitKey(1)&255==ord("q"): break
cap.release(); cv2.destroyAllWindows()
