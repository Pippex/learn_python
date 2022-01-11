import pickle
import random


class Idols():
    def __init__(self, name, universe, characteristic):
        self.__name = name
        self.__universe = universe
        self.__characteristic = characteristic

    def status(self):
        return {"Name":self.__name,
                "Universe":self.__universe,
                "Characteristic":self.__characteristic}


class Idols_list():
    def __init__(self):
        self.__list = []
        try:
            idols_file = open("idols_file", "rb")
            for i in pickle.load(idols_file):
                self.__list.append(i)
                
            print(f"{len(self.__list)} people have been added from extern file")

            for i in self.__list:
                print(i.status())

        except FileNotFoundError:
            print("There is no external file")
            external_file = open("idols_file", "wb")
            external_file.close()
            del(external_file)

    def append_idol(self, idol):
        self.__list.append(idol)
        with open("idols_file", "rb+") as idols_file:
            pickle.dump(self.__list, idols_file)

    def pop_idol(self, idol):
        find_pop_idol = []
        for i in self.__list:
            find_pop_idol.append(i.status())

        print(f"\n {find_pop_idol} \n")
        
        try:
            remove_index = find_pop_idol.index(idol.status)
            del self.__list[remove_index]
            print(f"{idol.status()} deleted from the file")
        except ValueError:
            print("This idols isn't in the file")
        idols_file = open("idols_file", "rb+")
        pickle.dump(self.__list, idols_file)
        idols_file.close()

    def view_idols(self):
        viewable_list = []
        for i in self.__list:
            viewable_list.append(i.status())

        return viewable_list
        

my_idols = Idols_list()
# # fitz = Idols("Fitz Chivalry Farseer", "The Elderlings Realm", "Skilled")
edward = Idols("Edward Elric", "Full Metal Alchemist (Brotherhood)", "Alchemist")
# my_idols.append_idol(fitz)
# my_idols.append_idol(edward)
my_idols.pop_idol(edward)
my_idols.pop_idol(edward)
my_idols.pop_idol(edward)
my_idols.pop_idol(edward)


print(my_idols.view_idols())