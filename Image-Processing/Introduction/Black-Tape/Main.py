import cv2

# Read the image
image = cv2.imread("simons.jpg")

# Resize the image to 440x600
resize_img = cv2.resize(image, (440, 600))

# Convert the resized image to grayscale
gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)

# Draw a black diagonal line
x = 0
for i in range(160):
    gray_img[115-x:160-x, 0+x:1+x] = 0
    if x >= 115:
        gray_img[0:160-x, 0+x:1+x] = 0
    x += 1

# Display the modified image
cv2.imshow("black-tape", gray_img)

# Save the modified image
cv2.imwrite("black-tape.jpg", gray_img)

# Wait for a key press to close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
