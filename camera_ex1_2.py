
# Question 1 of task 4
#This funciton track  the color object with hsv
import cv2
import numpy as np

def track_object():
    #Start video capture from  webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not accessible")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture video")
            break

        # Convert frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # HSV range for orange color
        lower_limits = np.array([5, 100, 100])
        upper_limits = np.array([15, 255, 255])

        # Create a mask for orange color
        mask = cv2.inRange(hsv_frame, lower_limits, upper_limits)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # draw bounding box around the largest contour
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame and mask
        cv2.imshow('Frame', frame)
        
        # Break the loop with the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

track_object()




# #this code is for tracking the object using RBG
# import cv2
# import numpy as np

# def track_object_in_rgb():
#     # Start video capture from the first connected webcam
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Error: Camera not accessible")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Unable to capture video")
#             break

#         # define RGB range for orange color
#         lower_limits = np.array([0, 100, 200], dtype="uint8")
#         upper_limits = np.array([100, 200, 255], dtype="uint8")

#         # Create a mask for orange color
#         mask = cv2.inRange(frame, lower_limits, upper_limits)

#         # Find contours in the mask
#         contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#         # Draw bounding box around the largest contour
#         if contours:
#             largest_contour = max(contours, key = cv2.contourArea)
#             x, y, w, h = cv2.boundingRect(largest_contour)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

#         # Display the resulting frame and mask
#         cv2.imshow('Frame', frame)
        
#         # Break the loop with the 'q' key
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the capture and close all windows
#     cap.release()
#     cv2.destroyAllWindows()

# track_object_in_rgb()


# Using HSV is typically more effective than RGB for color-based object tracking due to 
# its ability to better handle variations in lighting and environmental conditions.


# The threshold range in the code for an orange object is defined as:
# Lower Limits: [5, 100, 100] (in HSV)
# Upper Limits: [15, 255, 255] (in HSV)
# This range is relatively narrow, indicating a specific hue for orange, 
# but it's large in saturation and value. 


# Question 2 of task 4:  Is there a major difference in the tracking ability of your object?
# For RBG it was a major difference but for HSV it was not a mjoar difference. 