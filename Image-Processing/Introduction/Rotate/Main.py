import cv2

# Read the image from file
image = cv2.imread("sad-men.jpg")

# Resize the image to 1000x600 pixels
sad_man_img = cv2.resize(image, (1000, 600))

# Rotate the image by 180 degrees
happy_man_img = cv2.rotate(sad_man_img, cv2.ROTATE_180)

# Display the rotated image in a window named "Happy_Men"
cv2.imshow("Happy-Men", happy_man_img)

# Save the rotated image as "happy_man.jpg"
cv2.imwrite("happy-men.jpg", happy_man_img)

# Wait for a key press to close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
