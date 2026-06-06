yearly_subscription = int(input())

trainers = 0.60 * yearly_subscription
equipment = 0.80 * trainers
ball = 0.25 * equipment
accessories = 0.20 * ball

total_amount = (yearly_subscription + trainers + equipment + ball + accessories)

print(f"{total_amount:.2f}")