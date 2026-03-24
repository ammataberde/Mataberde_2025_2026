import math
g = 9.8

angle = int(input("Enter launch angle (degrees): "))
distance = int(input("Enter maximum distance (meters): "))
radians = math.radians(angle)
initial_velocity = math.sqrt((distance * g) / math.sin(2 * radians))
final_velocity = f"{initial_velocity:.2f}"


print("Required Launch Speed: ",final_velocity, "m/s")
