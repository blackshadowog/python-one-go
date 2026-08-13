import cv2,numpy as np,glob
board=(9,6)
obj=np.zeros((board[0]*board[1],3),np.float32); obj[:,:2]=np.mgrid[0:9,0:6].T.reshape(-1,2)
objs=[]; imgs=[]
for f in glob.glob("calibration_images/*.jpg"):
    im=cv2.imread(f); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ok,c=cv2.findChessboardCorners(g,board,None)
    if ok: objs.append(obj); imgs.append(c)
if not imgs: raise RuntimeError("No checkerboard found")
_,K,D,_,_=cv2.calibrateCamera(objs,imgs,g.shape[::-1],None,None)
print("Camera Matrix:\n",K); print("Distortion:\n",D)
