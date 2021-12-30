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
            if only_item and i == len(string) - 1:
                if string[i-1] == " ":
                    item_positions.append(i)
            elif only_item and i == 0:
                if string[i+1] == " ":
                    item_positions.append(i)
            elif only_item:
                if string[i-1] == string[i+1] == " ":
                    item_positions.append(i)
    
    return item_positions
    
print(position_string("a a a a a a a a a  a  a a  a    a", "a", only_item=True))

#Ugh, this is a lot of if's, I wil try to optimize it