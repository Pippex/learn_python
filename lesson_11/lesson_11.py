class house():
    surface = 100
    color = "Red"
    doors = 3
    trees = 10

    def create_door(self):
        self.doors += 1

    def how_many_doors(self):
        return f"This object has {self.doors} doors"

my_house = house()
print(my_house.color)
my_house.color = "Green"
print(my_house.color)
my_house.rooms = 10
print(my_house.rooms)
my_house.create_door()
print(my_house.doors)
print(my_house.how_many_doors())