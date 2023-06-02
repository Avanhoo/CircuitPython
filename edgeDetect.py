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
cv2.imshow('Canny Edge Detection', edges) # Display Canny Edge Detection Image

cv2.waitKey(0)
cv2.imwrite('edge.jpg', edges)


merge = cv2.addWeighted(img_gray, .75, edges, .25, 0.0)
cv2.imshow('Merged', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()