operations = ["Addition", "Sustraction", "Division", "Multiplication"]

def calculator(num1, num2, operation):
    if operation == 0:
        return num1 + num2
    elif operation == 1:
        return num1 - num2
    elif operation == 2:
        try:
            return num1/num2
        except ZeroDivisionError:
            return "You cann't divide by zero, do you want to break the world?"
    else:
        return num1*num2

num1 = "Hello"
num2 = "World"
operation = 23

while True:
    try:
        num1 = float(input("Input a number please: "))
        num2 = float(input("Input a second number please: "))
        break
    
    except ValueError:
        print("Please enter valid numbers")

    finally:
        print("\n")

choose_operation_counter = False

while not(-1 < operation < 4) or type(operation) != int:
    if choose_operation_counter:
        print("Please input a valid operation")
    for i in range(len(operations)):
        print(f"{i+1}. {operations[i]}")
    
    operation = int(input("What operation do you want to perform on these numbers? ")) - 1
    choose_operation_counter = True

print(calculator(num1, num2, operation))

def i_hate_19(num1, num2, operation):
    if calculator(num1, num2, operation):
        raise ValueError("I hate 19")
try:
    i_hate_19(num1, num2, operation)

except ValueError as fuck_you_19:
    print(f"I hate the fucking 19 \n {fuck_you_19}")