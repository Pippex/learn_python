names_lastnames = {"Constanza":"Patent",
                    "Felipe":"Vazquez"
}

def name_of_child(name):
    child = name +" "+ names_lastnames["Felipe"] +" "+ names_lastnames["Constanza"]
    return child

print(name_of_child("Traspie"))

names_lastnames["Traspie"] = "Vatidico"
print(names_lastnames)
del names_lastnames["Traspie"]
print(names_lastnames)

print(names_lastnames.keys())
print(names_lastnames.values())
print(names_lastnames.items())
print(names_lastnames.get("Felipe"))

#This follow the next structure
#The dictionary "game_items" has 3 dictionarys inside of them
#"Weapons", "Armors", "Potions"
#In each one we have all the items of this category
#And a list with characteristics of this item
#List Weapons: [attack, durability, required level, price]
#list Armors: [defense, durability, required level, price]
#list Potions: [potion type, effect, required level, price]

potions_types = ["Attack", "Defense", "Stamine", "Life"]

game_items = {"Weapons":{"Wood Sword": [5, 20, 1, 10],
                         "Stone Sword": [7, 25, 5, 20],
                         "Iron Sword": [10, 30, 10, 50],
                         "Diamond Sword": [15, 50, 30, 300]},
              "Armors": {},
              "Potions": {}}

print(game_items["Weapons"]["Wood Sword"])