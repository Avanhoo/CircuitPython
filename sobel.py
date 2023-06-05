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
cap = cv2.VideoCapture(0) # Camera is 480 x 640

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 960), fx = 0, fy = 0) # Enlarges the video 
 
    frame = frame.astype('uint8') #MAYBE
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Does edge detection in b&w
    blur = cv2.GaussianBlur(gray, (3,3), 0) 

    edges = cv2.Sobel(src=blur, ddepth=2, dx=1, dy=1, ksize=5)
    #edgesB = cv2.GaussianBlur(edges, (3,3), 0) # Makes edge smoother
    #edges = cv2.addWeighted(edges, 1, edgesB, 1, 0.9) # Makes a "glowing" edge
    edges = cv2.merge((edges,edges,edges))
    edges = edges.astype('uint8') #MAYBE
   

    merge = cv2.addWeighted(frame, 1, edges, 1, 0.0)
    #merge = cv2.resize(merge, (1280, 960), fx = 0, fy = 0) # Enlarges the video 
    cv2.imshow('Video',merge)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
quit()


