import cv2
import numpy as np
import argparse
import glob

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

# Read the original image
cap = cv2.VideoCapture('sample.mp4') # Camera is 480 x 640

while True:
    ret, frame = cap.read()
    
    frame = cv2.resize(frame, (1280, 960), fx = 0, fy = 0) # Enlarges the video 
    dimensions = frame.shape
 


    frame = frame.astype('uint8') #MAYBE
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(frame, (3,3), 0) 

    edges = auto_canny(blur) # Canny edge detection
    edgesB = cv2.GaussianBlur(edges, (3,3), 0) # Makes edge smoother
    edges = cv2.addWeighted(edges, 1, edgesB, 1, 0.9) # Makes a "glowing" edge
    edges = cv2.merge((edges,edges,edges))
   

    merge = cv2.addWeighted(frame, 1, edges, 1, 0.0)
    cv2.imshow('Video',merge)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
quit()












'''
height, width, number of channels in image
height = frame.shape[0]
width = frame.shape[1]
channels = frame.shape[2]

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)'''