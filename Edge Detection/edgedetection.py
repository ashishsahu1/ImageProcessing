import cv2
import numpy as np

img=cv2.imread('pt.jpg')

'''cv2.imshow('Image',img)
k=cv2.waitKey(0) & 0xFF
if k==27: 
    cv2.destroyAllWindows()'''

edged = cv2.Canny(img,100,200)

cv2.imshow('Edge Image',edged)
k=cv2.waitKey(0) & 0xFF
if k==27: 
    cv2.destroyAllWindows()


    