# import the opencv library 
import cv2 
# define a video capture object 
vid = cv2.VideoCapture(0) 

while(True): 
	
	# Capture the video frame 
	# by frame 
	ret, frame = vid.read() 
	edged=cv2.Canny(frame,100,200)
	# Display the resulting frame 
	cv2.imshow('Frame',frame)
	cv2.imshow('Edged', edged)

	if cv2.waitKey(1) & 0xFF == ord('c'):
		cv2.imwrite("Capture." + '.' + ".jpg",edged)

	
	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 
	if cv2.waitKey(1) & 0xFF == ord('q'): 
		break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
