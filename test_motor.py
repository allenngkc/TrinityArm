from viam.components.motor import Motor; 

from angle_determine import determine_absolute_arm_angles

REVOLUTIONS_PER_DEGREE = 0.1; 

def convert_deg_angle_to_revolutions(deg_angle): 
    return deg_angle * REVOLUTIONS_PER_DEGREE

first_rot_motor = Motor("anu2003motor-left")

target_first_angle = determine_absolute_arm_angles(6, 50)[0]

target_rev = convert_deg_angle_to_revolutions(target_first_angle)

print(f"Going to {target_first_angle}")
first_rot_motor.go_to(target_rev)
print("Finished")

