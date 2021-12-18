def salaries_logic():
    ceo_wage = int(input("Input the salary of the CEO: "))
    secretary_wage = int(input("Input the salary of the secretary: "))
    janitor_wage = int(input("Input the salary of the janitor: "))

    if janitor_wage < secretary_wage < ceo_wage:
        print("Salaries make sense")
    
    else:
        print("This salaries doesn't make sense")


#salaries_logic()

def scholarship_elegibility(wage, grade):
    
    #if (wage < 1000 and grade > 8) or (wage < 2500 and grade > 9.5):
    if wage < 1000 and grade > 8 or wage < 2500 and grade > 9.5:
        return "Elegible for scholaship"
    else:
        return "Not elegible for scholarship"


print(f"Juan Mendoza is {scholarship_elegibility(800, 9.2)}")
print(f"Jorge Garcia is {scholarship_elegibility(2000, 10)}")

disponible_subjects = ["MATH", "SING", "WRITING", "READING", "SOCCER"]

def favorite_subject():
    subject = (input(f"What of this subjects is your favorite? {disponible_subjects}: "))
    
    if subject.upper() in disponible_subjects:
        print(f"Oh, your favorite subject is {subject}, me too!")
    
    else:
        print("This subject does not exist")
        favorite_subject()


favorite_subject()
