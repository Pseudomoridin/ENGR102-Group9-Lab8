# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 8 challenge
# Date:         October 28, 2021

# imports
import math as m

# method definition
def interpolate(temp1, temp2, temp, pressure):
    tempdiff = float(temp2) - float(temp1)
    tempratio = (float(temp) - float(temp1))/tempdiff
    properties = []
    for i in range(4):
        twopressures = []
        for j in range(2):
            propertyprime = (pressureList[j][temp2][i] - pressureList[j][temp1][i]) * tempratio + pressureList[j][temp1][i]
            twopressures.append(propertyprime)
        pressurediffratio = (float(pressure) - 5) / 5
        propertydiff = twopressures[1] - twopressures[0]
        property = twopressures[0] + (propertydiff * pressurediffratio)
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

tenMPa = {
    # "Sat" : [0.0014522, 1393.3, 1407.9, 3.3603],
    "0" : [0.0009952, 0.12, 10.07, 0.0003],
    "20" : [0.0009973, 83.31, 93.28, 0.2943],
    "40" : [0.0010035, 166.33, 176.37, 0.5685],
    "60" : [0.0010127, 249.43, 259.55, 0.826],
    "80" : [0.0010244, 332.69, 342.94, 1.0691],
    "100" : [0.0010385, 416.23, 426.62, 1.2996],
    "120" : [0.0010549, 500.18, 510.73, 1.5191],
    "140" : [0.0010739, 584.72, 595.45, 1.7293],
    "160" : [0.0010854, 670.06, 681.01, 1.9316],
    "180" : [0.0011200, 756.48, 767.68, 2.1271],
    "200" : [0.0011482, 844.32, 855.8, 2.3174],
    "220" : [0.0011809, 934.01, 945.82, 2.5037],
    "240" : [0.0012192, 1026.2, 1038.3, 2.6876],
    "260" : [0.0012653, 1121.6, 1134.3, 2.871],
}

pressureList = [fiveMPa, tenMPa]

# Initial input
temperature = float(input("Enter a temperature between 0 and 260 deg C: "))
pressure = float(input("Enter a pressure between 5 and 10 MPa: "))
temp = temperature # Will hold range values of temperature
keys = list(fiveMPa.keys())

# Changing temp from float to temperature range
for i in range(len(keys) - 1):
    if int(keys[i]) <= temperature <= int(keys[i + 1]):
        temp = [keys[i], keys[i + 1]]

# Interpolation
properties = interpolate(temp[0], temp[1], temperature, pressure)

# Output
print("Properties at {:.1f} deg C and {:.1f} MPa are:".format(temperature, pressure))
print("Specific volume (m^3/kg): {:.7f}".format(properties[0]))
print("Specific internal energy (kJ/kg): {:.2f}".format(properties[1]))
print("Specific enthalpy (kJ/kg): {:.2f}".format(properties[2]))
print("Specific entropy (kJ/kgK): {:.4f}".format(properties[3]))