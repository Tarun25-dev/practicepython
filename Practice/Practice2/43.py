# Problem:
# Given temperature in Celsius, convert to Fahrenheit and Kelvin.
# Formulas: F = C * 9/5 + 32 | K = C + 273.15

c = float(input())
f = c * 9/5 +32
k = c + 273.15
print("temperature in fahrenheit:",f,"F")
print("temperature in kelvin:",k,"K")