import pickle
import random as rd

bools = [True, False]

class Pippex_lovers():
    def __init__(self, name, pippex_relationship, tula, nice_ass= bools[rd.randint(0,1)]):
        self.__name = name.capitalize()
        self.__pippex_relationship = pippex_relationship
        self.__fucking_with_pippex = False
        self.__nice_ass = nice_ass
        self.__dick = tula

    def botox(self):
        self.__nice_ass = True

    def pippex_want_to_fuck(self):
        if not self.__dick and self.__nice_ass:
            self.__fucking_with_pippex = True
        else:
            self.__fucking_with_pippex = True

    def status(self):
        return {"Name": self.__name,
                "Pippex relationship": self.__pippex_relationship,
                "Fucking with Pippex": self.__fucking_with_pippex,
                "Nice ass": self.__nice_ass,
                "Dick": self.__dick}


hobbys = ["Invest in crypto", "Listen to music", "Be a mathematician", "FUCK WITH THE MARKET"]

with open("Pippex's_hobbys", "wb") as binary_file:
    pickle.dump(hobbys, binary_file)
    

with open("Pippex's_hobbys", "rb") as binary_file:
    pippex_is_god = pickle.load(binary_file)
    print(pippex_is_god)

pray_to_pippex = "PIPPEX IS MY GOD, I LOVE PIPPEX, I WANT TO FUCK WITH PIPPEX"

with open("i_love_pippex", "wb") as binary_pray:
    binary_file = pickle.dump(pray_to_pippex, binary_pray)

#with open("i_love_pippex", "ab") as binary_pray:
#    binary_file = pickle.dump("PIPPEX PLEASE DESTROY MY ASS", binary_file)

with open("i_love_pippex", "rb") as binary_pray:
    print(pickle.load(binary_pray))

Edward = Pippex_lovers("Edward Elric", "Friend", True)
Lust = Pippex_lovers("Lust", "Friend", False)

pippex_fuckers = [Edward, Lust]

with open("Pippex_fuckers", "wb") as fuckers_binary:
    fuckers_binary = pickle.dump(pippex_fuckers, fuckers_binary)

fuckers_binary = open("Pippex_fuckers", "rb")
my_fuckers = pickle.load(fuckers_binary)

del(fuckers_binary)
print(my_fuckers[1].status())