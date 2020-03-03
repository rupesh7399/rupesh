import cv2
import numpy as np 

# Create a black image
image = np.zeros((512,512,3), np.uint8)

# #Can we make this in black and white?
# image_bw = np.zeros((512,512 ), np.uint8)

# cv2.imshow("Black Rectangle (Color)", image)
# cv2.imshow("Black Rectangle (B&W)", image_bw)

# cv2.line(image, (0,0), (511,511), (255,217,0),5)
#cv2.rectangle(image, (100,100), (300,250), (217,50,127), -1)
#cv2.circle(image,(350, 350), 100, (15,75,50), -1)

##Let's define four points
#pts = np.array([[10,500], [300,50],[300,300],[50,500]], np.int32)
#
## Let's now reshape our points in form required by polylines
#pts = pts.reshape((-1,1,2))
#
#cv2.polylines(image, [pts], True, (0,0,255), 3)
#######################################3
cv2.putText(image, 'Hello World!' , (75,290), cv2.FONT_HERSHEY_COMPLEX, 2,(100,170,0), 3)

cv2.imshow("Polygon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()