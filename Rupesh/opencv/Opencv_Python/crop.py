import cv2
import numpy as np

image = cv2.imread('/home/vrs0023/Pictures/gettyimages-1081754182-2048x2048.jpg')
height, width = image.shape[:2]

# Let's get the starting pixel coordiantes (top Left of cropping rectangle)
start_row, start_col = int(height * .70), int(width * .25)

# Let's get the ending pixel coordinates (bottom right)
end_row, end_col = int(height *.75), int(width *.50)

# Simply use indexing to crop out the rectangle we desire
cropped = image[start_row:end_row, start_col:end_col]

cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()