from viam.components.motor import Motor; 

from angle_determine import determine_absolute_arm_angles

# x value left right 
# z close far 
# Smaller the bounding box, farther away


bounding_box_area = 330

k = 0.567

distance = k / bounding_box_area 