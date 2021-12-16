important_dates = ["06/12/2021", "13/12/2021"]

print(important_dates[0])

all_names = ["Constanza", "Patent", "Garcia", "Juan", "Felipe", "Vazquez", "Balderas"]


def name_constanza():

    print(f"Constanza's name is {all_names[0:3]}")


name_constanza()


def name_felipe():
    print(f"Felipe's name is {all_names[3:8]}")


name_felipe()

print(all_names[3:])
print(all_names[:3])

def print_names():

    print(f"{all_names[0]} and {all_names[4]}")


print_names()

names_dates = all_names + important_dates

print(names_dates)

names_dates.append("16/12/2021")

print(names_dates)

important_dates.append("16/12/2021")

print(important_dates)

important_dates.insert(0, "23/09/2006")

print(important_dates)

important_dates.insert(1, "03/12/2021")

print(important_dates)

important_dates.extend(["17/12/2021", "18/12/2021"])

print(important_dates)

print(important_dates.index("03/12/2021"))

print("10/12/2021" in important_dates)
print("03/12/2021" in important_dates)

important_dates.remove("03/12/2021")

print(important_dates)

important_dates.remove(important_dates[4])

print(important_dates)

important_dates.pop()

print(important_dates)

important_dates += names_dates

print(important_dates)