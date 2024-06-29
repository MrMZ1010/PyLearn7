import cv2
import numpy as np

# Create a black 560x560 image
chess_board = np.zeros((560, 560))

# Iterate over 8x8 grid to create the chessboard pattern
for i in range(8):
    for j in range(8):
        # Set the white squares
        if (i + j) % 2 == 0:
            chess_board[70*i:70*(i+1), 70*j:70*(j+1)] = 255

# Display the chessboard image
cv2.imshow("chess-board", chess_board)

# Save the chessboard image
cv2.imwrite('chess-board.jpg', chess_board)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

