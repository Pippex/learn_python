class Home():
    def __init__(self, surface, color):
        self.__surface = surface
        self.__color = color
        self.__money = 200
        self.__water_service = True
        self.__electric_service = True
        self.__internet_service = False
    
    def __check_money(self, spend_money):
        can_spend = self.__money >= spend_money
        if can_spend:
            self.__money -= spend_money
        return can_spend
    
    def contract_internet(self, *args):
        if len(args) == 1:
            if self.__internet_service != args[0] == True and self.__check_money(120):
                self.__check_money(120)
                self.__internet_service = True

            if self.__internet_service != args[0] == False:
                self.__check_money(-120)
                self.__internet_service = False
            
        if self.__internet_service:
            return "You have internet service"

        else:
            return "You don't have internet service"

    def status(self):
        return {"Surface":self.__surface,
                "Color":self.__color,
                "Money":self.__money,
                "Water Service":self.__water_service,
                "Electric Service":self.__electric_service,
                "Internet Service":self.__internet_service}
        
class Apartment(Home):
    def __init__(self, surface, color, floor):
        super().__init__(surface, color)
        self.__floor = floor

    def status(self):
        return {"Surface":self.__surface,
                "Color":self.__color,
                "Money":self.__money,
                "Water Service":self.__water_service,
                "Electric Service":self.__electric_service,
                "Internet Service":self.__internet_service,
                "Floor": self.__floor}
    

class House(Home):
    def __init__(self, surface, color):
        super().__init__(surface, color)
        self.grass_height = 10
    
    def cut_lawn(self, want_to_cute=False):
        if want_to_cute:
            self.grass_height -= 5
        return f"The grass height is {self.grass_height}"

    def status(self):
        return {"Surface":self.__surface,
                "Color":self.__color,
                "Money":self.__money,
                "Water Service":self.__water_service,
                "Electric Service":self.__electric_service,
                "Internet Service":self.__internet_service,
                "Grass Height":self.grass_height}


class Penthouse(Home):
    def __init__(self, surface, color, number_employees):
        super().__init__(surface, color)
        self.__employees = number_employees
    
    def add_fire_employee(self, number=0):
        self.__employees += number
        return f"The penthouse has {self.employees} employees"

    def status(self):
        return {"Surface":self.__surface,
                "Color":self.__color,
                "Money":self.__money,
                "Water Service":self.__water_service,
                "Electric Service":self.__electric_service,
                "Internet Service":self.__internet_servic,
                "Employees":self.__employees}


class Mansion(Penthouse, House):
    def __init__(self, surface, color, number_employees):
        super().__init__(surface, color, number_employees)
        self.grass_height = 10
    

