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
choose_numbers_counter = False
operation = 23

while type(num1) != float or type(num2) != float:
    if choose_numbers_counter:
        print("Please input valid numbers")
    try:
        num1 = float(input("Input a number please: "))
        num2 = float(input("Input a second number please: "))
    except ValueError:
        pass
    choose_numbers_counter = True

choose_operation_counter = False

while not(-1 < operation < 4) or type(operation) != int:
    if choose_operation_counter:
        print("Please input a valid operation")
    for i in range(len(operations)):
        print(f"{i+1}. {operations[i]}")
    
    operation = int(input("What operation do you want to perform on these numbers? ")) - 1
    choose_operation_counter = True

print(calculator(num1, num2, operation))