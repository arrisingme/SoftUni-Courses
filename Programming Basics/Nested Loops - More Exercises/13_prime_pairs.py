start_1st_pair = int(input())
start_2nd_pair = int(input())
diff_1st = int(input())
diff_2nd = int(input())

end_1st_pair = start_1st_pair + diff_1st
end_2nd_pair = start_2nd_pair + diff_2nd

for d1 in range(start_1st_pair, end_1st_pair + 1):
    is_prime_1st = True
    if d1 < 2:
        is_prime_1st = False
    else:
        for i in range(2, int(d1 ** 0.5) + 1):
            if d1 % i == 0:
                is_prime_1st = False
                break

    if is_prime_1st:
        for d2 in range(start_2nd_pair, end_2nd_pair + 1):
            is_prime_2nd = True
            if d2 < 2:
                is_prime_2nd = False
            else:
                for j in range(2, int(d2 ** 0.5) + 1):
                    if d2 % j == 0:
                        is_prime_2nd = False
                        break

            if is_prime_2nd:
                print(str(d1) + str(d2))
