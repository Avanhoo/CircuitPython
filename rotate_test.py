import cv2
import numpy as np

img = cv2.imread('test.jpg')
cv2.imshow("og",img)
img_cw_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.namedWindow("Full", cv2.WINDOW_KEEPRATIO)
cv2.setWindowProperty("Full", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Full", img_cw_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
