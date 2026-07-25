list_of_integers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

sorted_list = sorted(list_of_integers)
to_remove = sorted_list[:numbers_to_remove]

numbers_left = [x for x in list_of_integers if x not in to_remove]

print(", ".join(map(str, numbers_left)))