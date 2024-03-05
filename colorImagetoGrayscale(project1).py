import numpy as np
import cv2

path = input("Enter the path and name of image:")
print("you enter this path:",path)

#now read image take path from user
#cnvert color to gray image
#project 1
# how to save output image in folder
img = cv2.imread(path,0)
img1= cv2.resize(img,(500,500))
print(img1)
cv2.imshow("color to gray",img1)
k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite(".\image\output.png", img)
else:
    cv2.destroyAllWindows()


