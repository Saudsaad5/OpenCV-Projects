import cv2 as cv

# Uncomment below to read and display an image from file
# img = cv.imread('../imgs/IMG_9644.png')
# if img is None:
#     print("Image not found. Check the path!")
# else:
#     cv.imshow('Img', img)
#     cv.waitKey(0)


# Start video capture from the default camera (usually webcam)
cap = cv.VideoCapture(0)

while True:
    # Read a frame from the camera
    isTrue, frame = cap.read()

    # Display the frame in a window named 'Video'
    cv.imshow('Video', frame)

    # Exit loop if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv.destroyAllWindows()


