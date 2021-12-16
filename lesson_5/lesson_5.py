names_lastnames = {"Constanza":"Patent",
                    "Felipe":"Vazquez"
}

def name_of_child(name):
    child = name +" "+ names_lastnames["Felipe"] +" "+ names_lastnames["Constanza"]
    return child

print(name_of_child("Traspie"))