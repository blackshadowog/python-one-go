import cv2,time
face=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0); last=time.time()
while True:
    ok,f=cap.read()
    if not ok: break
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY); faces=face.detectMultiScale(g,1.1,6)
    for x,y,w,h in faces: cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
    now=time.time(); fps=1/max(now-last,.001); last=now
    cv2.putText(f,f"Faces: {len(faces)}  FPS: {fps:.1f}",(20,40),0,.8,(255,255,255),2)
    cv2.imshow("Vision Dashboard",f)
    if cv2.waitKey(1)&255==ord("q"): break
cap.release(); cv2.destroyAllWindows()
