print('Welcome to the tip calculator.')
price = float(input('What was the total bill?\n'))
number_of_people = int(input("How many people to split the bill?\n"))
tip_percent = int(input("What pwrcentage tip would you like to give? 10, 12 or 15?\n"))


if tip_percent in [10, 12, 15]:
   
    tip_percent = (tip_percent/100) + 1
else:
    print("Type a valid tip percentage. ")

print(type(price), type(number_of_people), type(tip_percent))

price_per_person = (price * tip_percent) /number_of_people
print(f'Each person should pay: {price_per_person}')