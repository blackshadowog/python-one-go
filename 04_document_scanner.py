import cv2,numpy as np
img=cv2.imread("document.jpg")
img=cv2.resize(img,(800,int(img.shape[0]*800/img.shape[1])))
e=cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),(5,5),0),75,200)
cs,_=cv2.findContours(e,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
page=None
for c in sorted(cs,key=cv2.contourArea,reverse=True)[:10]:
    a=cv2.approxPolyDP(c,.02*cv2.arcLength(c,True),True)
    if len(a)==4: page=a.reshape(4,2); break
if page is None: raise RuntimeError("Document not found")
def order(p):
    r=np.zeros((4,2),np.float32); s=p.sum(1); d=np.diff(p,axis=1).ravel()
    r[0]=p[np.argmin(s)]; r[2]=p[np.argmax(s)]; r[1]=p[np.argmin(d)]; r[3]=p[np.argmax(d)]
    return r
M=cv2.getPerspectiveTransform(order(page),np.array([[0,0],[800,0],[800,1100],[0,1100]],np.float32))
out=cv2.warpPerspective(img,M,(800,1100)); cv2.imwrite("scanned.jpg",out)
cv2.imshow("Scanner",out); cv2.waitKey(0); cv2.destroyAllWindows()
