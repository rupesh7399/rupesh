import cv2
import numpy as np

# We need to import matploatlib to create our histogram plots
from matplotlib import pyplot as plt

# image = cv2.imread('./images/input.jpg')
# histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# # We ploat a histogram, ravel() flatens our image array
# plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# #Viewing Separate Color Channels
# color = ('b', 'g', 'r')

# # We now separate the colors and plot each in the Histogram 
# for i, col in enumerate(color):
    # histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    # plt.plot(histogram2, color = col)
    # plt.xlim([0,256])

# plt.show()

image = cv2.imread('./images/tobago.jpg')
cv2.imshow('Tobego',image)
cv2.waitKey(0)


histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# We plot a histogram, ravel() flatens our image array
plt.hist(image.ravel(), 256, [0, 256]); plt.show()

# Viewing Separate Color Channels
color = ('b','g', 'r')

#We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0, 256])

plt.show()


