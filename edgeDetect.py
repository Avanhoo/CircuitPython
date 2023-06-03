import cv2
import numpy as np

# Read the original image
img = cv2.imread('test.jpg')

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display greyscale image
cv2.imshow('Grey', img_gray)
cv2.waitKey(0)
 
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0) 
 
 
edges = cv2.Canny(image=img_blur, threshold1=65, threshold2=10) # Canny Edge Detection
#edgesB = cv2.GaussianBlur(edges, (3,3), 0) # Makes edge smoother
#edges = cv2.addWeighted(edges, 1, edgesB, 1, 0.9) # Makes a "glowing" edge
edges = cv2.merge((edges,edges,edges))
   
cv2.imshow('Canny Edge Detection', edges) # Display Canny Edge Detection Image

cv2.waitKey(0)
cv2.imwrite('edge.jpg', edges)


merge = cv2.addWeighted(img, 1, edges, 1, 0.0)
cv2.imshow('Merged', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()