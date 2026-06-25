number_of_strings = int(input())
given_word = input()
strings_list = []

for string in range(number_of_strings):
    current_string = input()
    strings_list.append(current_string)

filtered_string = []

for word in strings_list:
    if given_word in word:
        filtered_string.append(word)

print(strings_list)
print(filtered_string)



# number_of_strings = int(input())
# given_word = input()
# strings_list = []
#
# for string in range(number_of_strings):
#     current_string = input()
#     strings_list.append(current_string)
#
# filtered_string = []
#
# for word in strings_list:
#     if given_word in word:
#         filtered_string.append(word)
#
# print(strings_list)
# print(filtered_string)





# number_of_strings = int(input())
# given_word = input()
# strings_list = []
#
# for string in range(number_of_strings):
#     current_string = input()
#     strings_list.append(current_string)
# print(strings_list)
#
# for string in range(len(strings_list) -1, -1, -1):
#     element = strings_list[string]
#     if given_word not in element:
#         strings_list.remove(element)
# print(strings_list)
