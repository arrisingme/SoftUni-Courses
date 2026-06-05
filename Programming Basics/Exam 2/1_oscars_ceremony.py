rent = int(input())

statuette = 0.70 * rent
catering = 0.85 * statuette
sound = 0.50 * catering

total_expense = (rent + statuette + catering + sound)

print(f"{total_expense:.2f}")