import cv2 as cv

img = cv.imread('../imgs/IMG_6557.png')

if img is None:
    print("Image not found. Check the path!")
else:
    cv.imshow('Img', img)
    cv.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    # Rescale the frame by the given scale factor
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Rescaled Img', rescaleFrame(img))
cv.waitKey(0)