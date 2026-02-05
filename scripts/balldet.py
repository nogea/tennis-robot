import cv2
import numpy as np

# print(cv2)
# print(cv2.__file__)
# print("VideoCapture" in dir(cv2))


# Load a video file
cap = cv2.VideoCapture(
    "/media/shivaram/data1/Tennis/test_94638.mp4"
)
# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()  

# Read the frames from the video
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) if fps > 0 else 33

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Caanny Edge Detection (commented out)
    edges = cv2.Canny(blurred_frame, 50, 150)

    # Find all closed contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #Spit out the smaller contours
    for contour in contours:
        if cv2.contourArea(contour) < 50 and cv2.contourArea(contour) > 10:
            # continue
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower_yellow = np.array([0, 150, 120])
    # upper_yellow = np.array([80, 250, 190])
    # mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    # result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame', frame)
    # cv2.imshow('Blurred Grayscale Frame', blurred_frame)
    # cv2.imshow('Canny Edges', edges)
    # cv2.imshow('Tennis Ball Tracking', result)

    # if cv2.waitKey(delay) & 0xFF == ord('q'):
    #     break
    #Take the image after 2 seconds
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
