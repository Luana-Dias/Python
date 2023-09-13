year = int(input('Type any year: '))
is_leap = None

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False 
    else:
        is_leap = True 
else: 
    is_leap = False 

if is_leap == False:
    print('This is NOT a leap year')
elif is_leap == True:
    print('This is a leap year')
