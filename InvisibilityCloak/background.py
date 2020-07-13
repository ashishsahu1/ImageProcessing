#------------------------------------------------------------------------------
#first step is to click a background image
#second step select the colour
#it should remove every pixel which is red and change with background
#------------------------------------------------------------------------------

#importing libraries
import cv2
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,back=cap.read()#reading from webcam 
    #ret is true if camera is recalled otherwise its false
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5)==ord('q'):
            # when pressed q save the image
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()
