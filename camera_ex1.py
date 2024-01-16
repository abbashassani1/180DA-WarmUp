import cv2
import numpy as np

# create a function to track the object
def track_object(frame, lower_color, upper_color, color_space = 'HSV'):
    if color_space == 'HSV':
        # needs to convert to HSV color space
        converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    else:
        # Use RGB color space
        converted_frame = frame

    # create a mask with the specified color range
    mask = cv2.inRange(converted_frame, lower_color, upper_color)

    # find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw bounding box around the largest contour
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

# start capturing video from a webcam
cap = cv2.VideoCapture(0)

# set the color range for tracking
# HSV color range for a blue object
lower_color = np.array([110, 50, 50])
upper_color = np.array([130, 255, 255])

try:
    while True:
        # capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # track the object
        frame = track_object(frame, lower_color, upper_color, color_space = 'HSV')

        # display the resulting frame
        cv2.imshow('Object Tracking', frame)

        # break the loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # release the capture
    cap.release()
    cv2.destroyAllWindows()
