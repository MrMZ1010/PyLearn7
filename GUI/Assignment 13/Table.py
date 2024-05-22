##### Mohammad Ali Mirzaei #####

import arcade

COLUMN_SPACING = 45
ROW_SPACING = 45
margin_left = 50
margin_bottom = 50

arcade.open_window(500, 500, "Complex Loops - Box")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * COLUMN_SPACING + margin_left
        y = row * ROW_SPACING + margin_bottom
        if column%2==0 and row%2==0  or column%2==1 and row%2==1:
            arcade.draw_triangle_filled(x-7,y, x, y+7,x+7,y, arcade.color.RED)
            arcade.draw_triangle_filled(x-7,y, x, y-7,x+7,y, arcade.color.RED)           
        if column%2==1 and row%2==0  or column%2==0 and row%2==1:
            arcade.draw_triangle_filled(x-7,y, x, y+7,x+7,y, arcade.color.BLUE)
            arcade.draw_triangle_filled(x-7,y, x, y-7,x+7,y, arcade.color.BLUE)
arcade.finish_render()
arcade.run()
