import numpy as np
import cv2

def empty():
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cv2.namedWindow('TrackBar')
#cv2.resizeWindow('TrackBar',(640,300))
cv2.createTrackbar('Hue min','TrackBar',4,179,empty)
cv2.createTrackbar('Hue max','TrackBar',13,179,empty)
cv2.createTrackbar('Sat min','TrackBar',71,255,empty)
cv2.createTrackbar('Sat max','TrackBar',255,255,empty)
cv2.createTrackbar('Val min','TrackBar',109,255,empty)
cv2.createTrackbar('Val max','TrackBar',255,255,empty)


img=cv2.imread('5.jpeg')

while True:
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos('Hue min','TrackBar')
    h_max=cv2.getTrackbarPos('Hue max','TrackBar')
    s_min=cv2.getTrackbarPos('Sat min','TrackBar')
    s_max=cv2.getTrackbarPos('Sat max','TrackBar')
    v_min=cv2.getTrackbarPos('Val min','TrackBar')
    v_max=cv2.getTrackbarPos('Val max','TrackBar')

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imageResult=cv2.bitwise_and(img,img,mask=mask)

    imgStack = stackImages(0.6,([img,imgHSV],[mask,imageResult]))


    '''cv2.imshow('Output',img)
    cv2.imshow('HSV Output',imgHSV)
    cv2.imshow('Mask Output',mask)
    cv2.imshow('Result',imageResult)'''
    cv2.imshow("Final",imgStack)
    cv2.waitKey(1)