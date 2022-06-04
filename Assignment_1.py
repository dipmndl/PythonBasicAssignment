''' 1.  Write a Python program to print "Hello Python"?'''
print("Hello Python")

''' 2.  Write a Python program to do arithmetical operations addition and division.? '''
a = 10
b =  20
print(f"Addition is: {a+b}")
print(f"Division is: {b/a}")

''' 3.  Write a Python program to find the area of a triangle?'''
a = 10
b = 15
c = 20
# Calculate the semi perimeter
s = (a+b+c)/2
area_trngle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(f"Area of a triangle is {area_trngle}")

''' 4.  Write a Python program to swap two variables?'''
x = 10
y = 20
temp = x
x = y
y = temp
print(f"The value of X after swaping {x}")
print(f"The value of Y after swaping {y}")
'' '5.  Write a Python program to generate a random number?'''
import random
# print(f"random number between 0 to 9 {random.randint(1,10)}")
random_list = []
for i in range(0,5):
    n = random.randint(1,10)
    random_list.append(n)

print(f"Ranandom number between 0 to 9 {random_list}")

