import numpy as np      
import cv2      
#Color Image        
img = cv2.imread("./image/test.jpg",1) 
img1 = cv2.resize(img,(500,500))
img2 = cv2.flip(img1,0)
print(img)
cv2.imshow('Colored image', img2) 


#grayScale Image
img = cv2.imread("./image/test.jpg",0) 
img1 = cv2.resize(img,(500,500))
print(img)
cv2.imshow('Gray image', img1) 

#unchanged Image
img = cv2.imread("./image/test.jpg",-1) 
img1 = cv2.resize(img,(500,500))
print(img)
cv2.imshow('Unchanged image', img1) 


cv2.waitKey(0)
cv2.destroyAllWindows()
 





