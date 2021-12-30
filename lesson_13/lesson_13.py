hello_world = "This is the first thing that a programer student does, print a message \
that says 'Hello World'"

print(hello_world)
print(hello_world.count("Hello World"))
print(hello_world.find("Hello World"))
print(hello_world.isdigit())
print(hello_world.isalnum())
print(hello_world.isalpha())
print("Hello".isalpha())
print("1923".isalnum())
print("109238".isdigit())
print(hello_world.split("W"))
print(hello_world.find("a"))
print(hello_world.count("a"))

#I'll create a funtion for search all the a's positions in the string

def position_string(string, item_searched, only_item=False):
    item_positions = []
    for i in range(len(string)):
        if string[i] == item_searched:
            if only_item and i == len(string) - 1 and string[i-1] == " ":
                item_positions.append(i)
            elif only_item and i == 0 and string[i+1] == " ":
                item_positions.append(i)
            elif only_item and string[i-1] == string[i+1] == " ":
                item_positions.append(i)
            elif not only_item:
                item_positions.append(i)
    
    return item_positions
    
print(position_string("a a a a a a a a a  a  a a  a    a", "a", only_item=True))

#Ugh, this is a lot of if's, I wil try to optimize it
#Mmn, this is not "Optimize", but at least it no longer has a lot of ifs

print("aa 3".isalnum())

#I'll create a function to comprobate if a email address is correct or not

def correct_email(email):
    has_at = False
    ats_all = position_string(email, "@")
    if len(ats_all) == 1:
        if 0 != ats_all[0] and ats_all[0] != len(email)-1:
            has_at = True

    return has_at

if correct_email(input("Please input your email address: ")):
    print("Your email is correct")

else:
    print("Your email isn't correct")