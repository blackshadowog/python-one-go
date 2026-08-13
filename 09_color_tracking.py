import cv2,numpy as np
cap=cv2.VideoCapture(0)
while True:
    ok,f=cap.read()
    if not ok: break
    h=cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    m=cv2.inRange(h,np.array([0,120,70]),np.array([10,255,255]))|cv2.inRange(h,np.array([170,120,70]),np.array([180,255,255]))
    cs,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if cs and cv2.contourArea(max(cs,key=cv2.contourArea))>500:
        c=max(cs,key=cv2.contourArea); (x,y),r=cv2.minEnclosingCircle(c)
        cv2.circle(f,(int(x),int(y)),int(r),(0,255,0),2)
    cv2.imshow("Red Tracking",f)
    if cv2.waitKey(1)&255==ord("q"): break
cap.release(); cv2.destroyAllWindows()
