no_remove = (7, 14, 23)

print(no_remove)
print(no_remove[1])

print(12 in no_remove)

lists_in_tuple = ([3, 7, 21], [9, 20, 10], [3, 5, 8])

print(lists_in_tuple)

tuples_in_tuple = (lists_in_tuple, no_remove)

print(tuples_in_tuple)

lists_in_lists = list(lists_in_tuple)

print(lists_in_lists)

lists_in_lists.pop()

print(lists_in_lists)

again_lists_in_tuple = tuple(lists_in_lists)

print(again_lists_in_tuple)

print(4 in again_lists_in_tuple)

print(again_lists_in_tuple.count(10))
print(again_lists_in_tuple.count([3, 7, 21]))

print(len(lists_in_tuple))
print(len(lists_in_tuple[1]))

my_name = ("Felipe",)
your_name = ("Constanza",)

print(f"{my_name} and {your_name} are friends")

first_list, second_list = again_lists_in_tuple

print(f"This is the first list {first_list} and this is the second list {second_list}")

print(no_remove.index(7))