import math

max_x_value = 30

def convert_to_angle(x_value, z_value): 
    res = math.degrees(math.atan(z_value / x_value))   
    if (res < 0): 
        res = 180 + res
    return round(res, 2)     

print("x=-2, z=3", convert_to_angle(-2, 3))
print("x=2, z=3", convert_to_angle(2, 3))
print("x=-3, z=5", convert_to_angle(-3, 5))