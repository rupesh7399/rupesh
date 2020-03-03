import cv2
import numpy as np
input = cv2.imread('./images/input.jpg')
#cv2.imshow('hello world', input)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#print(input.shape)
# print('Height of Image:',int(input.shape[0]),'pixels')
# print('Width of Image:',int(input.shape[1]),'pixels')
cv2.imwrite('output.jpg',input)
cv2.imwrite('output.png',input)