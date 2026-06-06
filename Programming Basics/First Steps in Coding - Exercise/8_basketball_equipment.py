yearly_tax = int(input())

shoes = yearly_tax - (yearly_tax * 0.40)
equipment = shoes - (shoes * 0.20)
ball = equipment * 0.25
accessories = ball * 0.20

total_amount = shoes + equipment + ball + accessories + yearly_tax

print(total_amount)
