import numpy as np 
import cv2


# Function we'll use to display contours area

def get_contour_areas(contours):
    # return the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

#Load our image
image = cv2.imread('images/bunchofshapes.jpg')
orginal_image = image

# Let's print the ateas of the contours before sorting
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find Canny edges
edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Contors Areas before sorting", get_contour_areas(contours))

# Sort contours latge to small
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
#sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]

print("Contor Areas after sorting", get_contour_areas(sorted_contours))

# Iterate over our contours and draw one at a time
for c in sorted_contours:
    cv2.drawContours(orginal_image, [c], -1, (255,0,0),3)
    cv2.waitKey(0)
    cv2.imshow('Contours by area', orginal_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


