import cv2
import numpy as np 

# Function we'll use for sorting by position

def x_cord_contour(countours):
    # Returns the X cordinate for the contour centroid
    if cv2.contourArea(countours)>10:
        M = cv2.moments(countours)
        return(int(M['m10']/M['m00']))

def label_contour_center(image, c, i):
    # Plase a red circle on the centers of contours
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    # Draw the countour number on the image
    cv2.circle(image,(cx,cy), 10, (0,0,255), -1)
    return image

# Load our image
image = cv2.imread('images/bunchofshapes.jpg')
orginal_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 50, 200)
#cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Computer Center of mass or centroids and draw them on our image
for (i, c) in enumerate(contours):
    orig = label_contour_center(image, c, i)

cv2.imshow("4 - Contour Centers", image)
cv2.waitKey(0)

# Sort by left to right using our x_cord_contour function
contours_left_to_right = sorted(contours, key= x_cord_contour, reverse=False)
# Labeling Contours left to right
for (i,c) in enumerate(contours_left_to_right):
    cv2.drawContours(orginal_image, [c],-1,(0,0,255),3)
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv2.putText(orginal_image, str(i+1), (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    cv2.imshow('6 - left to Right Contour', orginal_image)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(c)

    #Let's now crop each contour and save these images
    cropped_contour = orginal_image[y:y + h, x:x + w]
    image_name = 'output_shape_number_' + str(i+1) + '.jpg'
    print(image_name)
    cv2.imwrite(image_name, cropped_contour)
cv2.destroyAllWindows()