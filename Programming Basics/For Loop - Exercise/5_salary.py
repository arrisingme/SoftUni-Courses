tabs_opened = int(input())
salary = int(input())
if_salary_not_0 = True

for i in range(tabs_opened):
    new_tab = input()
    if new_tab == "Facebook":
        salary -= 150
    elif new_tab == "Instagram":
        salary -= 100
    elif new_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        if_salary_not_0 = False
        break

if if_salary_not_0:
    print(salary)