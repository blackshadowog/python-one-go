import cv2
img=cv2.imread("shapes.png")
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(g,120,255,cv2.THRESH_BINARY)
cs,_=cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in cs:
    if cv2.contourArea(c)<100: continue
    p=cv2.arcLength(c,True); a=cv2.approxPolyDP(c,.04*p,True)
    x,y,w,h=cv2.boundingRect(c); n=len(a)
    name="Triangle" if n==3 else "Quadrilateral" if n==4 else "Circle/Polygon"
    cv2.drawContours(img,[c],-1,(0,255,0),2)
    cv2.putText(img,name,(x,y-10),0,.6,(255,0,0),2)
cv2.imshow("Shapes",img); cv2.waitKey(0); cv2.destroyAllWindows()
