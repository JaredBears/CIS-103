wage = float(input('What is your hourly wage? '))
reg_hours = float(input('How many regular hours did you work? '))
over_hours = float(input('How many overtime hours did you work? '))
reg_pay = reg_hours * wage
over_pay = over_hours * wage * 1.5
total_pay = reg_pay + over_pay
print(f'Your total pay is ${total_pay:.2f}')
