import cv2

# Load the image
image = cv2.imread('C:\\Users\\abbas\\Downloads\\cat.png')

# Check if the image was successfully loaded
if image is None:
    print("Could not open or find the image.")
else:
    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # # Display the original image
    # cv2.imshow('Original Image', image)

    # # Display the Grayscale image
    # cv2.imshow('Grayscale Image', gray_image)

    # # Display the HSV image
    # cv2.imshow('HSV Image', hsv_image)

    # # Wait for a key press indefinitely
    cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()

#Filtering the based on color(Thresholding)
# Convert to a binary image using thresholding
# Load the image
image_path = 'C:\\Users\\abbas\\Downloads\\cat.png'
image = cv2.imread(image_path)

# Check if image is loaded properly
if image is None:
    print(f"Could not open or find the image at path: {image_path}")
else:
    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert to a binary image using thresholding
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # # Display the original image
    # cv2.imshow('Original Image', image)

    # # Display the binary image
    # cv2.imshow('Binary Image', binary_image)

    # Wait for a key press to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import numpy as np
if image is None:
    print("Could not open or find the image.")
else:
    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of color you want to filter
    # For example, let's filter for red
    # Adjust the HSV values according to the color you want to filter
    lower_red = np.array([20, 10, 0])  # Lower range of HSV values for red
    upper_red = np.array([180, 180, 200])  # Upper range of HSV values for red

    # Create a mask with the specified color range
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Apply the mask to the original image
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    # Display the original image
    # cv2.imshow('Original Image', image)

    # # Display the mask
    # cv2.imshow('Mask', mask)

    # # Display the filtered color image
    # cv2.imshow('Filtered Color Image', filtered_image)

    # Wait for a key press indefinitely
    cv2.waitKey(0)

    # Destroy all windows
    cv2.destroyAllWindows()


#edge detetion
# Load the image
image_path = 'C:\\Users\\abbas\\Downloads\\cat.png'
image = cv2.imread(image_path)

# Check if image is loaded properly
if image is None:
    print(f"Could not open or find the image at path: {image_path}")
else:
    # Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Using Canny edge detection
    edges = cv2.Canny(gray_image, 20, 10)

    # # Display the original image
    # cv2.imshow('Original Image', image)

    # # Display the edges
    # cv2.imshow('Edges', edges)

    # Wait for a key press to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#templete matching
    
# Load the main image and convert to grayscale
image_path = 'C:\\Users\\abbas\\Downloads\\cat.png'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the template image (make sure it is in grayscale)
template_path = 'C:\\Users\\abbas\\Downloads\\catcopy.png'
template = cv2.imread(template_path, 0)  # '0' loads it in grayscale

# Template matching
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Normalize the result
cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX)

# Find the maximum value (best match) and its location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the matched region
top_left = max_loc  # Change to min_loc for other methods like TM_SQDIFF
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
cv2.rectangle(gray_image, top_left, bottom_right, 255, 2)

# Display the original image with the rectangle
#cv2.imshow('Detected', gray_image)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

#convex hall/ boundary contours

# Assuming 'binary_image' is already created and processed

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Load the original image to draw on
original_image = cv2.imread('C:\\Users\\abbas\\Downloads\\cat.png')

# Draw contours
cv2.drawContours(original_image, contours, -1, (0, 255, 0), 3)

# Find and draw convex hull
for cnt in contours:
    hull = cv2.convexHull(cnt)
    cv2.drawContours(original_image, [hull], -1, (0, 0, 255), 3)

# Assuming there is at least one contour, draw bounding box for the first contour
if contours:
    x, y, w, h = cv2.boundingRect(contours[0])
    cv2.rectangle(original_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the image with drawn contours, convex hulls, and bounding box
#cv2.imshow('Contours, Convex Hulls, and Bounding Box', original_image)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

#video part
import cv2
import numpy as np

# Function to detect the gesture (simple motion detection)
def detect_gesture(frame, prev_frame):
    # Process the frames to detect motion (this is a placeholder - actual implementation will vary)
    # Return True if gesture is detected, False otherwise
    pass

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

prev_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV (for color tracking)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of color to track
    lower_color = np.array([10, 100, 50])  # Example values
    upper_color = np.array([205, 255, 180])

    # Threshold the HSV image to get only the desired color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Optional: Draw contours on the frame
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(f"Object coordinates: {x}, {y}")  # Print object coordinates

    # Gesture Detection
    if prev_frame is not None:
        if detect_gesture(frame, prev_frame):
            print("Gesture detected!")

    prev_frame = frame.copy()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop with the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()
