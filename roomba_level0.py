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
speed(1)

right(90)
forward(40)
 
# End your code here
###
 
window.exitonclick()