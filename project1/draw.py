import cv2 as cv
import numpy as np

# Create a blank 500x500 image with 3 color channels (RGB), filled with zeros (black)
blank = np.zeros((500, 500, 3), dtype='uint8')

# Fill a rectangular region with green color
blank[200:300, 300:400] = 0, 255, 0

# Draw a filled blue rectangle from top-left (0,0) to bottom-right (250,250)
cv.rectangle(blank, (0,0), (250,250), (255, 0, 0), thickness=cv.FILLED)

# Draw a filled red circle at the center (250,250) with radius 40
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=cv.FILLED)

# Draw a white diagonal line from top-left to bottom-right
cv.line(blank, (0,0), (500, 500), (255, 255, 255), thickness=3)

# Draw a white diagonal line from bottom-left to top-right
cv.line(blank, (0,500), (500, 0), (255, 255, 255), thickness=3)

# Put green text on the image at position (250,100)
cv.putText(blank, "Hello From Saud", (150,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,255), 2)

# Display the image in a window
cv.imshow('img', blank)
cv.waitKey(0)