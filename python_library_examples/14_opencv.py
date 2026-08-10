import cv2

img = cv2.imread("image.jpg")
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.jpg", gray)
    print("Image converted to grayscale.")
else:
    print("Put image.jpg in this folder first.")
