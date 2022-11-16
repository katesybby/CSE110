print ("Welcome to the velocity calculator. Please enter the following:")
print()
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Cross sectional area (in m^2): "))
constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print ()

import math
c = (1 / 2) * density * area * constant
#v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
v = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c)/mass) * time))

print (f"The inner value of c is: {c:.3f}")
print (f"The velocity after 10.0 seconds is: {v:.3f} m/s")

v_terminal = math.sqrt((mass * gravity)/ c) 
print(f"Terminal velocity is {v_terminal:.3f}")