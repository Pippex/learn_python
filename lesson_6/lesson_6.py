frequent_questions = {"What is your name?": "My name is Constanza",
                      "What do you like to do?": "I like to read, sing and eat",
                      "What is your full name?": "Constanza Patent Vatidico"}

def question():
    ask = input("Would you like to do a question? [Y/N] ")
    if ask == "Y":
        print((frequent_questions[input("Ok, tell me your question: ")]))
        question()


question()

number = 5

def play_game():
    estimation = int(input("Ok, I am thinking a number[1-10], guess which one is: "))
    if estimation == number:
        print("YES!. That's my number")
    elif estimation < number:
        print("Oh, no, that number is lower than mine")
        play_game()
    else:
        print("Oh, no, that number is higer than mine")
        play_game()
    
play_game()

def max_return():
    first_number = int(input("Input a number: "))
    second_number = int(input("Input a number: "))
    number_return = 0

    if first_number > second_number:
        number_return = first_number

    elif first_number == second_number:
        number_return = "These number are the same"
    
    else:
        number_return = second_number

    return number_return

print(max_return())