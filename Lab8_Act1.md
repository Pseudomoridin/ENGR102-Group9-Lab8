# Lab 8 Data
## Pressure: 5 MPa
### Celcius : \[v in m^3/kg, u in kJ/kg, h in kJ/kg, s in kJ/(kg*K)\]
- "Sat." : \[0.0012862, 1148.1, 1154.5, 2.9207],
- "0" : \[0.0009977, 0.04, 5.03, 0.0001\],
- "20" : \[0.0009996, 83.61, 88.61, 0.2954\],
- "40" : \[0.0010057, 166.92, 171.95, 0.5705\],
- "60" : \[0.0010149, 250.29, 255.36, 0.8287\],
- "80" : \[0.0010267, 333.82, 338.96, 1.0723\],
- "100" : \[0.0010410, 417.65, 422.85, 1.3034\],
- "120" : \[0.0010576, 501.91, 507.19, 1.5236\],
- "140" : \[0.0010769, 586.8, 592.18, 1.7344\],
- "160" : \[0.0010988, 672.55, 678.04, 1.9374\],
- "180" : \[0.0011240, 759.47, 765.09, 2.1338\],
- "200" : \[0.0011531, 847.92, 853.68, 2.3251\],
- "220" : \[0.0011868, 938.39, 944.32, 2.5127\],
- "240" : \[0.0012268, 1031.6, 1037.7, 2.6983\],
- "260" : \[0.0012755, 1128.5, 1134.9, 2.8841\],

## Pressure: 10 MPa
### (Celcius, v in m^3/kg, u in kJ/kg, h in kJ/kg, s in kJ/(kg*K))
- "Sat" : \[0.0014522, 1393.3, 1407.9, 3.3603\],
- "0" : \[0.0009952, 0.12, 10.07, 0.0003\],
- "20" : \[0.0009973, 83.31, 93.28, 0.2943\],
- "40" : \[0.0010035, 166.33, 176.37, 0.5685\],
- "60" : \[0.0010127, 249.43, 259.55, 0.826\],
- "80" : \[0.0010244, 332.69, 342.94, 1.0691\],
- "100" : \[0.0010385, 416.23, 426.62, 1.2996\],
- "120" : \[0.0010549, 500.18, 510.73, 1.5191\],
- "140" : \[0.0010739, 584.72, 595.45, 1.7293\],
- "160" : \[0.0010854, 670.06, 681.01, 1.9316\],
- "180" : \[0.0011200, 756.48, 767.68, 2.1271\],
- "200" : \[0.0011482, 844.32, 855.8, 2.3174\],
- "220" : \[0.0011809, 934.01, 945.82, 2.5037\],
- "240" : \[0.0012192, 1026.2, 1038.3, 2.6876\],
- "260" : \[0.0012653, 1121.6, 1134.3, 2.871\],

# Lab 8 Pseudocode
## Process
- Dictionary
    - Hard-coded
    - Values the rest of the program will use stored here
    - To retrieve a value, use dictionary[temperature]
- Interpolation
    - Make a line between two known points, then use line to find properties
        - use y = slope(x - pointx) + pointy
    - Challenge
        - Use same process as above, but three times (total):
            - Once each to get the properties at 5 MPa and 10 MPa
            - Interpolate between the two to get properties at selected pressure
- Input
    - Input temp, format so that it is a string
- Output
    - Output properties individually based on interpolated values

## Variables
- float temperature
- str[] temperature range (min, max)
- float[] properties (v, u, h, s)
- Challenge specific:
    - float pressure
    - float[] properties1 (v, u, h, s)
    - float[] properties2 (v, u, h, s)

## Test Cases
- T = :
    - 0
    - -1
    - 261
    - 1
    - 259
    - 110
    - 132
    - 213
    - True
    - abc
