import cv2
import numpy as np 
image = cv2.imread('images/input.jpg',0)

height, width = image.shape

# Extract Sobel Edges
scobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
scobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.imshow('Sobel X', scobel_x)
cv2.waitKey(0)
cv2.imshow('Sobel Y', scobel_y)
cv2.waitKey(0)

sobal_OR = cv2.bitwise_or(scobel_x, scobel_y)
cv2.imshow('sobel_OR', sobal_OR)
cv2.waitKey(0)

laplacian = cv2.Laplacian(image, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)


## Then, we need to provide two values: threshold1 and threshold2. Any gradient value larger than threshold2
# is considered to be edge. Any value below threshold1 is consideres not to be an edge.
#Values in between threshold1 and threshold2 are either classified as edges or non-edeges based on how their
#intesnsities are "connected". In this case, any gradient values below 60 are considered non-edges
#whereas any values above 120 are considered edges.

# Canny Edge Detection uses gradient values as thresholds 
# The first threshold gradient
canny = cv2.Canny(image, 20, 170)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()