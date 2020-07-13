import cv2
import numpy as np 

cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg')

while cap.isOpened():
    #take each frame
    ret,frame=cap.read()

#RGB:red,green,blue
#HSV:Hue(Colour),Saturation(What is the amount the colour sui mixed with white colour),
#Value(What is the amount the colour is mixed with black)

#Why HSV: Because we humans use kind of HSV colour format
#           not RGB colour format

#Luminous :How much light is projected in something

    if ret:
        #how to convert from RGB to HSV
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        

        #how to get the HSV value?
        # Lower: hue-10,100,100 | Higher:hue+10,255,255

        red=np.uint8([[[0,0,255]]]) #bgr value of red
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV) #getting the HSV value of red
        print(hsv_red)


        #threshold the HSV value to get only the red colour
        l_red=np.array([0,100,100])
        u_red=np.array([10,255,255])

        mask=cv2.inRange(hsv,l_red,u_red)
        #cv2.imshow("Masked",mask)

        part1=cv2.bitwise_and(back,back,mask=mask)
        #cv2.imshow("Part 1",part1)

        mask=cv2.bitwise_not(mask)

        part2=cv2.bitwise_and(frame,frame,mask=mask)
        #cv2.imshow("Maksed",part2)

        cv2.imshow("Cloak",part1+part2)


        if cv2.waitKey(5)==ord('q'):
            # when pressed q save the image
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()

