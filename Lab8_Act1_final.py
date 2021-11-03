# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 8
# Date:         October 28, 2021

# imports
import math as m

# method definition
def interpolate(temp1, temp2, temp):
    tempdiff = float(temp2) - float(temp1)
    tempratio = (float(temp) - float(temp1))/tempdiff
    properties = []
    for i in range(4):
        property = (fiveMPa[temp2][i] - fiveMPa[temp1][i]) * tempratio + fiveMPa[temp1][i]
        properties.append(property)
    return properties

# static variable declaration
fiveMPa = {
    # "Sat." : [0.0012862, 1148.1, 1154.5, 2.9207],
    "0" : [0.0009977, 0.04, 5.03, 0.0001],
    "20" : [0.0009996, 83.61, 88.61, 0.2954],
    "40" : [0.0010057, 166.92, 171.95, 0.5705],
    "60" : [0.0010149, 250.29, 255.36, 0.8287],
    "80" : [0.0010267, 333.82, 338.96, 1.0723],
    "100" : [0.0010410, 417.65, 422.85, 1.3034],
    "120" : [0.0010576, 501.91, 507.19, 1.5236],
    "140" : [0.0010769, 586.8, 592.18, 1.7344],
    "160" : [0.0010988, 672.55, 678.04, 1.9374],
    "180" : [0.0011240, 759.47, 765.09, 2.1338],
    "200" : [0.0011531, 847.92, 853.68, 2.3251],
    "220" : [0.0011868, 938.39, 944.32, 2.5127],
    "240" : [0.0012268, 1031.6, 1037.7, 2.6983],
    "260" : [0.0012755, 1128.5, 1134.9, 2.8841],
}

# Initial input
temperature = float(input("Enter a temperature between 0 and 260 deg C: "))
temp = temperature # Will hold range values of temperature
keys = list(fiveMPa.keys())

# Changing temp from float to temperature range
for i in range(len(keys) - 1):
    if int(keys[i]) <= temperature <= int(keys[i + 1]):
        temp = [keys[i], keys[i + 1]]

# Interpolation
properties = interpolate(temp[0], temp[1], temperature)

# Output
print("Properties at {:.1f} deg C are:".format(temperature))
print("Specific volume (m^3/kg): {:.7f}".format(properties[0]))
print("Specific internal energy (kJ/kg): {:.2f}".format(properties[1]))
print("Specific enthalpy (kJ/kg): {:.2f}".format(properties[2]))
print("Specific entropy (kJ/kgK): {:.4f}".format(properties[3]))