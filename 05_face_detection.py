import cv2
model=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    ok,f=cap.read()
    if not ok: break
    g=cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    for x,y,w,h in model.detectMultiScale(g,1.1,6,minSize=(60,60)):
        cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Face Detection",f)
    if cv2.waitKey(1)&255==ord("q"): break
cap.release(); cv2.destroyAllWindows()
