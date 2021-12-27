class house():
    surface = 100
    color = "Red"
    doors = 3
    trees = 10
    water_service = True
    internet_service = False
    electric_service = True

    def contract_internet(self, contract_status=internet_service):
        if type(contract_status) == bool:
            self.internet_service = contract_status
        
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
                           "Water Service":self.water_service,
                           "Internet Service":self.internet_service,
                           "Electric Service":self.electric_service}
        
        return characteristics
    

my_house = house()
print(my_house.color)
my_house.color = "Green"
print(my_house.color)
#my_house.rooms = 10
#print(my_house.rooms)
my_house.create_door()
print(my_house.doors)
print(my_house.how_many_doors())
