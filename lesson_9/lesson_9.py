def pairs():
    num = 1
    while True:
        yield num*2
        num += 1


generator_pairs = pairs()
print(type(generator_pairs))


def three_multiples():
    num = 1
    while True:
        yield num*3
        num += 1


generator_three = three_multiples()

def four_multiples():
    num = 1
    while True:
        yield num*4
        num += 1


generator_four = four_multiples()

# old_f_1 = 1
# old_f_2 = 1
# def fibonacci_creator():
#     while True:
#         yield old_f_1 + old_f_2
    

# fibonacci = fibonacci_creator()

# while True:
#     print(next(fibonacci))

#Doesn't work

def lot_multiples(*multiples):
    for i in multiples:
        yield from i


lot_multiples(next(generator_pairs), next(generator_pairs),\
              next(generator_pairs), next(generator_pairs),\
              next(generator_three), next(generator_three),\
              next(generator_three), next(generator_three),\
              next(generator_four), next(generator_four),\
              next(generator_four), next(generator_four))

while True:
    print(next(lot_multiples()))