names = ["Constanza", "Paciencia", "Satoshi", "Hidalgo", "Veraz", "Traspie", "Ludwig"]

print(range(10))

def favorite_name():
    
    choosen_name = "Felipe"

    while choosen_name not in names:
        print("What of this is your favorite name?")

        for i in names:
            print(f"{i}, ", end="")
        
        choosen_name = input()

    print(f"Oh, your favorite name is {choosen_name}, me too!")

favorite_name()

def confirm_email(email):
    if "@" and "." in email:
        print("The email is correct")

    else:
        print("The email isn't correct")

shopping_list = []
shopping_list_upper = []

continue_adding = "Y"

while True:

    print("This is your shopping list")
    for i in shopping_list:
        print(i)


    add_item = input("What do you want to add?[Q for stop] ")
    
    if add_item.upper() == "Q":
        break
    elif add_item.upper() not in shopping_list_upper:
        shopping_list.append(add_item)
    else:
        print(f"{add_item} is already on your shopping list")
    
    shopping_list_upper.append(shopping_list[len(shopping_list) - 1].upper())

def multiples_range(start, finish, base):
    for i in range(start, finish, base):
        
        if finish - i > base:
            print(f"{i}, ", end= "")
        else:
            print(i)
    

multiples_range(int(input()), int(input()), int(input()))

def ignore_last(element):
    for i in element:
        if i == element[len(element)-1]:
            continue
        else:
            print(i)
    
ignore_last([1,2,3,4,5,6,7,8])

def number_letters(evaluate):
    letters = len(evaluate)
    for i in evaluate:
        if i != " ":
             continue
        else:
            letters -= 1
    return letters

print(number_letters("Hello World"))