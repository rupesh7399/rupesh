import cv2
import numpy as np 

image = cv2.imread('./images/input.jpg')
# height, width = image.shape[:2]

# # Divide by two to rototate the image around its center
# rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90,.5)

# rotated_image = cv2.warpAffine(image, rotation_matrix, (width,height))

# cv2.imshow('Rotated Image', rotated_image)

rotated_image = cv2.transpose(image)
cv2.imshow('Rotated Image - Method 2', rotated_image)

cv2.waitKey()
cv2.destroyAllWindows()