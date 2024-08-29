import math
from pydoc import importfile

Area_of_circle_rad_5 = math.pi * 5 ** 2
print("Area of Circle with a radius of 5 =",Area_of_circle_rad_5)
Volume_sphere_rad_3 = ((4 / 3) * math.pi * 3 ** 3)
print("Volume of sphere with a radius of 3 =",Volume_sphere_rad_3)
Hypo_right_tri_3_4= math.sqrt(3 ** 2 + 4 ** 2)
print("Hypotenuse of a right triangle with sides 3 and 4 =",Hypo_right_tri_3_4)
Thad_full = "ThaddeusChristopherLehmer"
print("My full name length =",len(Thad_full))
Thad_first_last = "Thaddeus" + " " + "Lehmer"
print("Uppercase name:", Thad_first_last.upper())
print("Lowercase name:",Thad_first_last.lower())
Thad_height=5.75
Thad_age=29
Thad_weight=180
Thad_BMI= (Thad_weight / ((Thad_height * 12) ** 2)) * 703
print("My Body Mass Index:",Thad_BMI)