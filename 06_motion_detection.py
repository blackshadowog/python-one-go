import cv2
cap=cv2.VideoCapture(0); prev=None
while True:
    ok,f=cap.read()
    if not ok: break
    g=cv2.GaussianBlur(cv2.cvtColor(f,cv2.COLOR_BGR2GRAY),(21,21),0)
    if prev is None: prev=g; continue
    d=cv2.dilate(cv2.threshold(cv2.absdiff(prev,g),25,255,cv2.THRESH_BINARY)[1],None,iterations=2)
    for c in cv2.findContours(d,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]:
        if cv2.contourArea(c)>800:
            x,y,w,h=cv2.boundingRect(c); cv2.rectangle(f,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Motion",f); prev=g
    if cv2.waitKey(1)&255==ord("q"): break
cap.release(); cv2.destroyAllWindows()
