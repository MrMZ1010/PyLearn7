import numpy as np
import cv2

# Create an empty 600x600 white image
letter_m_array = np.empty((600, 600))

# Set the entire image to white
letter_m_array.fill(255)

# Left and right lines of 'M'
for i in range(100, 501):
    for j, k in zip(range(80, 131), range(470, 521)):
        letter_m_array[i, j] = 0
        letter_m_array[i, k] = 0

# Bottom parts of the left and right lines
letter_m_array[501:505, 75:135] = 0
letter_m_array[501:505, 465:525] = 0

# Diagonal lines of 'M'
for i in range(100, 310):
    letter_m_array[i, i - 32:i + 32] = 0
    letter_m_array[i, 567 - i:631 - i] = 0

# Display the image
cv2.imshow("Letter M", letter_m_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image
cv2.imwrite("letter_M.jpg", letter_m_array)
