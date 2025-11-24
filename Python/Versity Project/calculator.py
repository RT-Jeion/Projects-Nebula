# python program to create a simple calculator

# 3 steps to build calculator program
#   1. functions for operations 
#   2. user input 
#   3. print result 

# step-1: create functions:
# Function to add two numbers 
def add(num1,num2):
     return num1 + num2 

# Function to substract two numbers 
def sub(num1,num2):
     return num1 - num2 

# Function to multiply two numbers 
def multiply(num1,num2):
     return num1 * num2  

# Function to divide two numbers 
def divide(num1,num2):
     return num1 / num2 

# Function to average two numbers 
def avg(num1,num2):
     return (num1 + num2)/2
# Function to get square root of a number
def square_root(number):
    import math
    return math.sqrt(number)


while True:
    print("\n\nPlease select a operation:\n" \
        "1. Addition\n" \
        "2. subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n" \
        "5. Average\n6. Square Root\n7. Quit") 

    select = input("Select a operation from 1,2,3,4,5,6: ")

    #Step-3: Print the result 
    if select == "1":
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        addition = add(number1, number2)

        print(number1, "+", number2, "= ", \
            addition)
        
    elif select == '2':
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        subtraction = sub(number1, number2)

        print(number1, "-", number2, "= ", \
            subtraction) 
        
    elif select == '3':
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        multiplication = multiply(number1, number2)

        print(number1, "*", number2, "= ", \
            multiplication)
        
    elif select == '4':
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        division = divide(number1, number2)
        print(number1, "/", number2, "= ", \
            division)

    elif select == '5':
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        average = avg(number1, number2)
        print("(",number1, "+", number2, ")", "/", "2", "= ", \
            average) 
        
    elif select == "6":
        number1 = int(input("Enter the Number: "))

        sq_root = square_root(number1)

        print(f"Square Root of {number1}: {sq_root}")


    elif select == '7':
        print("Closing Calculator.........")
        break
    else:
        print("Invalid operation! Pls select again!")
        