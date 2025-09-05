# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
speed(10)

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        forward(50)
        right(angle)

draw_shape(6)
draw_shape(5)
draw_shape(4)
draw_shape(3)
 
# End your code here
###
 
window.exitonclick()