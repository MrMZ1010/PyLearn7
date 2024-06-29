import cv2
import numpy as np

# Read the image from file
image = cv2.imread("woman.jpg")

# Invert the image using NumPy operations
inverted_image = 255 - image

# Display the inverted image in a window named "inverted_image"
cv2.imshow("inverted_image", inverted_image)

# Save the inverted image as "inverted_image.jpg"
cv2.imwrite("Emilia.jpg", inverted_image)

# Wait for a key press to close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
