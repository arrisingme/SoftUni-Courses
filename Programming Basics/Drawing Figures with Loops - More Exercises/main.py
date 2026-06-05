total_coffee = 0

command = input()
while command != "END":
    if command in ["coding", "dog", "cat", "movie"]:
        total_coffee += 1
    elif command in ["CODING", "DOG", "CAT", "MOVIE"]:
        total_coffee += 2

    command = input()

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)
