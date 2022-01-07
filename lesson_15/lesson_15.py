import io
from os import read

with open("hello_world.txt", "r") as hello_world:
    print(hello_world.read())
    print(hello_world.writable())
    print(hello_world.readable())
    print(hello_world.seekable())
    #hello_world.write(" Hello Mars, too")
    #print(hello_world.read())
    

with open("hello_mars.txt", "w") as hello_mars:
    hello_mars.write("Hello Mars, too")


pluton = open("FUCK_NON_PLANETS.txt", "w")

pluton.write("FUCK YOU PLUTON")

pluton.close()

with open("hello_mars.txt", "a") as hello_mars:
    hello_mars.write("\nHello Martians, too \nHello Everybody")

with open("hello_mars.txt", "r") as hello_mars:
    lines_hello_mars = hello_mars.readlines()

print(lines_hello_mars[2])

with open("all_numbers.txt", "w") as writing_numbers:
    for i in range(100):
        writing_numbers.write(f"{i} ")

with open("all_numbers.txt", "w") as writing_numbers:
    for i in range(100,102):
        writing_numbers.write(f"{i} ")

with open("all_numbers.txt", "r") as reading_numbers:
    print(reading_numbers.read())

with open("all_numbers.txt", "r") as reading_numbers:
    reading_numbers.seek(2)
    print(reading_numbers.read())