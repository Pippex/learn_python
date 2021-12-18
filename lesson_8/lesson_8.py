names = ["Constanza", "Paciencia", "Satoshi", "Hidalgo", "Veraz", "Traspie", "Ludwig"]

def favorite_name():
    
    choosen_name = "Felipe"

    while choosen_name not in names:
        print("What of this is your favorite name?")

        for name_for in names:
            print(name_for)
        
        choosen_name = input()

    print(f"Oh, your favorite name is {choosen_name}, me too!")