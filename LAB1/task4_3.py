
# Task 4: camera excercese 3 and the code from task 4 and question one

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

# Does changing your phone brightness help or hurt with how your code is able to track the color?
# The phone brights hurts becasuse the webcam cannot detect the color due to high brightness and this code is able to track the color so far.
