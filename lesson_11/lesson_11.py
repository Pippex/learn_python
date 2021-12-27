from typing import Container


class house():

    def __init__(self):
        self.surface = 100
        self.color = "Red"
        self.doors = 3
        self.trees = 10
        self.__water_service = True
        self.internet_service = False
        self.__electric_service = True


    def contract_internet(self, *args):
        if len(args) == 1:
            if type(args[0]) == bool:
                self.internet_service = args[0]
        
        if self.internet_service:
            return "You have internet service"
        else:
            return "You don't have internet service"


    def create_door(self, doors_to_create=0):
        self.doors += doors_to_create
        return f"This house has {self.doors} doors"


    def status(self):
        characteristics = {"Surface":self.surface,
                           "Color":self.color,
                           "Trees":self.trees,
                           "Water Service":self.__water_service,
                           "Internet Service":self.internet_service,
                           "Electric Service":self.__electric_service}
        
        return characteristics
    

my_house = house()
print(my_house.color)
my_house.color = "Green"
print(my_house.color)
#my_house.rooms = 10
#print(my_house.rooms)
my_house.create_door()
print(my_house.doors)
print(my_house.contract_internet(True))