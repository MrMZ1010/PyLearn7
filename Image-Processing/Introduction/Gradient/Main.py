import cv2
import numpy as np

# Create an array with values from 0 to 65024
array = np.arange(0, 65025, 1, np.uint8)

# Reshape the array into a 255x255 image
image = np.reshape(array, (255, 255))

# Print the array (optional for debugging)
print(array)

# Create a gradient effect
x = 0
for i in range(255):
    image[i, 0:255] = 255 - x
    x += 1

# Display the gradient image
cv2.imshow("Gradient", image)

# Save the gradient image
cv2.imwrite('gradient.jpg', image)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
