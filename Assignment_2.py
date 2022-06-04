
# 1. Write a Python program to convert kilometers to miles?
km_unit = float(input("Please enter Kilometer unit"))
convert_miles = 0.6214 * km_unit
print(f"The unit value in Miles is {convert_miles}")

# 2. Write a Python program to convert Celsius to Fahrenheit?
celcious_unit = int(input("Please enter temperature in Celcious"))
convert_fahrenheit = (celcious_unit*1.8) + 32
print(f"The temparature in Fahrenheit is {convert_fahrenheit}")


# 3. Write a Python program to display calendar?
import calendar
input_year = int(input("Please enter year"))
input_month = int(input("Please enter month"))
print(calendar.month(input_year,input_month))


# 4. Write a Python program to solve quadratic equation? ax2 + bx + c = 0, where a, b and c are real numbers and a ≠ 0
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
import cmath
a= 1 
b= 2 
c= 3
# calculate the discriminant
d  = (b**2) -(4*a*c)
sol1 = (-b + cmath.sqrt(d))/2*a
sol2 = (-b - cmath.sqrt(d))/2*a
print(f"The Solution are {sol1} and {sol2}")


# 5. Write a Python program to swap two variables without temp variable?
x = 10
y = 20
x, y = y, x 
print(f"The value of X after swaping {x}")
print(f"The value of Y after swaping {y}")
