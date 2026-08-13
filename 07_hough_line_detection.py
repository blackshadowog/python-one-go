import cv2,numpy as np
img=cv2.imread("road.jpg")
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); e=cv2.Canny(g,50,150)
lines=cv2.HoughLinesP(e,1,np.pi/180,80,minLineLength=80,maxLineGap=20)
if lines is not None:
    for x1,y1,x2,y2 in lines[:,0]: cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("Hough Lines",img); cv2.waitKey(0); cv2.destroyAllWindows()
