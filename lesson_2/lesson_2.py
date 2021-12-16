def favorite(thing, thing_type):
    print(f"{thing} is my favorite {thing_type}")


favorite("Bitcoin Cash", "Cryptocurrency")
favorite("Constanza", "girl")

def constanza_is(quality):
    print(f"Constanza is {quality}")


constanza_is("fifteen years old")


def comparate_ages(name_1, age_1, name_2, age_2):
    
    
    if age_1 > age_2:
        print(f"{name_1} is {age_1 - age_2} years older than {name_2}")
    

    elif age_1 == age_2:
        print(f"{name_1} is the same age as {name_2}")


    else:
        print(f"{name_2} is {age_2 - age_1} years older than {name_1}")


comparate_ages("Felipe", 15, "Constanza", 15)

def hello_constanza():
    print("Hello, my name is Constanza, I like to read, sing and eat")