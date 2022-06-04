""" # 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
input_number = float(input("Enter the number"))
if input_number < 0:
    print("Negative number")
elif input_number == 0:
    print("Zero number")
else:
    print("Positive number") """
# 2.	Write a Python Program to Check if a Number is Odd or Even?
""" input_number = int(input("Enter the number"))
if (input_number % 2) == 0 :
    print("Even number")
else:
    print("Odd number") """
# 3.	Write a Python Program to Check Leap Year?
""" def checkyear(year):
    if (year % 4 == 0) or (year % 400 == 0):
        print("Leap year")
    elif (year % 100 != 0):
        print("Not Leap year")
result = checkyear(2001) """

# 4.	Write a Python Program to Check Prime Number?
""" num = int(input("Enter the number"))
if num > 1:
    for i in range(2,num):
        if(num % i == 0): 
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

else:  # if num is less than or equal 1
    print(f"{num} is not a prime number")  """

# 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
p_num = []
for num in range(1,10000):
    if num > 1:
        for i in range(2,num):
            if(num % i == 0): 
                #print(f"{num} is not a prime number")
                break
        else:
            #print(f"{num} is a prime number")
            p_num.append(num)

    else:  # if num is less than or equal 1
        #print(f"{num} is not a prime number")
        pass

print(f"List of prime number is {p_num}")     

