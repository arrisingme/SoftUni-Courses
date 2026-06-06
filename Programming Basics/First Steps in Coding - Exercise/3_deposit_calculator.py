money = int(input())
period = int(input())
interest = float(input())/100

money_with_interest = money + period * ((money * interest)/12)

print(money_with_interest)