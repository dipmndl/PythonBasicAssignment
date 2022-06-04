#1.	Write a Python Program to Find the Factorial of a Number?

num = int(input("Enter the no"))
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

result = factorial(x= num)
print(f"Factorial of {num} is {result}")
#2.	Write a Python Program to Display the multiplication Table?
from itertools import count
num = int(input("Enter the no"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")

#3.	Write a Python Program to Print the Fibonacci sequence?
num = int(input("Enter the nth term"))
n1, n2 = 0 , 1
count = 0
if num <= 0:
    print("Please enter a positive number")
elif num ==1:
    num == 1
    print(f"Fibonacci sequence of {num} is 1")
elif num > 1:
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

#4.	Write a Python Program to Check Armstrong Number?
num = 111

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#5.	Write a Python Program to Find Armstrong Number in an Interval?
lower = 100
upper = 2000
for num in range(lower, upper + 1):
    # order of number
   order = len(str(num))
    # initialize sum
   sum = 0
   temp = num
   while temp > 0: 
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)
#6.	Write a Python Program to Find the Sum of Natural Numbers?
num = int(input("Enter the number"))
if num < 0:
    print("Enter a positive number")
else:
    result = (num*(num + 1))/2
    print(f"Sum of natural number is {result}")