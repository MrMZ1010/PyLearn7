##### Mohammad Ali Mirzaei #####

import arcade  # Import the arcade module for creating games

# Define constants for column and row spacing, as well as left and bottom margins
COLUMN_SPACING = 45
ROW_SPACING = 45
margin_left = 50
margin_bottom = 50

# Open a window with specified width, height, and title
arcade.open_window(500, 500, "Complex Loops - Box")

# Set the background color of the window to white
arcade.set_background_color(arcade.color.WHITE)

# Start the rendering process
arcade.start_render()

# Loop through rows
for row in range(10):
    # Loop through columns
    for column in range(10):
        # Calculate the x and y coordinates for the current column and row
        x = column * COLUMN_SPACING + margin_left
        y = row * ROW_SPACING + margin_bottom
        
        # Draw triangles based on column and row parity
        if column % 2 == 0 and row % 2 == 0 or column % 2 == 1 and row % 2 == 1:
            arcade.draw_triangle_filled(x - 7, y, x, y + 7, x + 7, y, arcade.color.RED)
            arcade.draw_triangle_filled(x - 7, y, x, y - 7, x + 7, y, arcade.color.RED)
        if column % 2 == 1 and row % 2 == 0 or column % 2 == 0 and row % 2 == 1:
            arcade.draw_triangle_filled(x - 7, y, x, y + 7, x + 7, y, arcade.color.BLUE)
            arcade.draw_triangle_filled(x - 7, y, x, y - 7, x + 7, y, arcade.color.BLUE)

# Finish the rendering process
arcade.finish_render()

# Run the game loop
arcade.run()

