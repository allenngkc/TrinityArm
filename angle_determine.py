import math


ARM_LENGTH = 5

# This determines the angle opposite to the desired distance side length
# Util method
def determine_angle_between_arms(desired_distance): 
    if desired_distance <= 2 * ARM_LENGTH: 
        return math.degrees(math.acos((2 * (ARM_LENGTH ** 2) - (desired_distance) ** 2) / (ARM_LENGTH ** 2 * 2)))
    return None

print("distance of 6", determine_angle_between_arms(6))
print("distance of 11", determine_angle_between_arms(11))
print("distance of 7", determine_angle_between_arms(7))
print("distance of 9", determine_angle_between_arms(9))
print("distance of 2", determine_angle_between_arms(2))


# Desired angle measured counter clockwise from positive x
def determine_arm_angles(desired_distance, desired_angle):
    first_arm_angle = (((180 - determine_angle_between_arms(desired_distance)) / 2) + desired_angle) % 360.0
    second_arm_angle = determine_angle_between_arms(desired_distance)
    return (first_arm_angle, second_arm_angle)

def determine_absolute_arm_angles(desired_distance, desired_angle): 
    first_arm_angle = (((180 - determine_angle_between_arms(desired_distance)) / 2) + desired_angle) % 360.0
    second_arm_angle = (180 - (determine_angle_between_arms(desired_distance) - first_arm_angle)) % 360.0
    return (first_arm_angle, second_arm_angle)

print("-"*50)
print("distance of 6 on 20 degrees in reach", determine_arm_angles(6, 20))
print("distance of 2 on 120 degrees in reach", determine_arm_angles(2, 120))
print("distance of 2 on 190 degrees in reach", determine_arm_angles(2, 190))
print("distance of 5 on 190 degrees in reach", determine_arm_angles(5, 190))
print("distance of 2 on 310 degrees in reach", determine_arm_angles(2, 310))

print("distance of 6 on 20 degrees in reach", determine_absolute_arm_angles(6, 20))
print("distance of 2 on 120 degrees in reach", determine_absolute_arm_angles(2, 120))
print("distance of 2 on 190 degrees in reach", determine_absolute_arm_angles(2, 190))
print("distance of 5 on 190 degrees in reach", determine_absolute_arm_angles(5, 190))
print("distance of 2 on 310 degrees in reach", determine_absolute_arm_angles(2, 310))



