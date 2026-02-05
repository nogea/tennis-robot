import cv2
import numpy as np

# import image called circles.jpg

image_path = '/media/shivaram/data1/Tennis/circles.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (9, 9), 2)
edges = cv2.Canny(blurred_image, 50, 150)

# Find all closed contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Draw all contours
for contour in contours:
    if cv2.contourArea(contour) < 60 and cv2.contourArea(contour) > 0:
        # continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Original Image', image)
# cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()