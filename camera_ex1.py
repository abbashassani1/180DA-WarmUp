# import cv2
# import numpy as np

# # create a function to track the object
# def track_object(frame, lower_color, upper_color, color_space = 'HSV'):
#     if color_space == 'HSV':
#         # needs to convert to HSV color space
#         converted_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     else:
#         # Use RGB color space
#         converted_frame = frame

#     # create a mask with the specified color range
#     mask = cv2.inRange(converted_frame, lower_color, upper_color)

#     # find contours in the mask
#     contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     # draw bounding box around the largest contour
#     if contours:
#         largest_contour = max(contours, key=cv2.contourArea)
#         x, y, w, h = cv2.boundingRect(largest_contour)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     return frame

# # start capturing video from a webcam
# cap = cv2.VideoCapture(0)

# # set the color range for tracking
# # HSV color range for a blue object
# lower_color = np.array([10, 100, 100])
# upper_color = np.array([20, 255, 255])

# try:
#     while True:
#         # capture frame-by-frame
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # track the object
#         frame = track_object(frame, lower_color, upper_color, color_space = 'HSV')

#         # display the resulting frame
#         cv2.imshow('Object Tracking', frame)

#         # break the loop with 'q'
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
# finally:
#     # release the capture
#     cap.release()
#     cv2.destroyAllWindows()


# source of this code is a youtube video
# https://www.youtube.com/watch?v=aFNDh5k3SjU
# import cv2
# import numpy as np
# from PIL import Image

# def get_limits(color):
#     c = np.uint8([[color]])
#     hsvC= cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
#     lowerLimit = hsvC[0][0][0] - 10, 100, 100
#     upperLimit = hsvC[0][0][0] + 10, 255, 255

#     lowerLimit = np.array(lowerLimit, dtype = np.uint8)
#     upperLimit = np.array(upperLimit, dtype = np.uint8)
#     return lowerLimit, upperLimit

# yellow = [0, 100, 250]
# cap = cv2.VideoCapture(0)


# while True:
#     ret, frame = cap.read()
#     cv2.imshow('Frame', frame)

#     hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     lowerLimit, upperLimit = get_limits(color = yellow)
#     mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)
#     mask_ = Image.fromarray(mask)

#     bound_box = mask_.getbbox()
#     print(bound_box)
#     if bound_box is not None:  # Change here
#         x1, y1, x2, y2 = bound_box
#         frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
 
#     cv2.imshow('Mask', frame)


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    # Directly use the BGR color for limits in RGB space
    # You need to define these limits based on the color you want to track
    lowerLimit = [color[0] - 10, color[1] - 10, color[2] - 10] # Adjust these values
    upperLimit = [color[0] + 10, color[1] + 10, color[2] + 10] # Adjust these values

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    return lowerLimit, upperLimit

# Define orange in BGR
orange = [0, 110, 250]  # This is a typical representation of orange in BGR
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    lowerLimit, upperLimit = get_limits(color=orange)
    mask = cv2.inRange(frame, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)

    bound_box = mask_.getbbox()
    print(bound_box)
    if bound_box is not None:
        x1, y1, x2, y2 = bound_box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('Mask', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
