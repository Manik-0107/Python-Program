# Calculate Sector area
# Area = ½ × r2 × θ
# r = radius
# θ = angle in radians

import math

r = float(input("\nPlease enter any radius for sector: "))
theta_deg = float(input("Please enter any angle: "))

theta_rad = math.radians(theta_deg)
area = 0.5 * r*r * theta_rad

print("The Sector area is: ", area, "\n")



"""
Please enter any radius for sector: 7
Please enter any angle: 80
The Sector area is:  34.208453339088855 

"""
