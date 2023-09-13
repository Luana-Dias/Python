print("Heloo! Welacome to the best Pizza store!")
size = input("Wich size wil you gave? [S, M, L]:_ ").lower().strip()
pepperoni = input('Will you have extra pepperoni?\nFor a small size is $2. Fora a medium ou large is $3 dollars. [Y, N]:_ ').lower().strip()
cheese = input("Wil you have extra cheese?\nFor a small pizza it`s $1, for a medium or large, it`s free. [Y, N]").lower().strip()
price = 0 

while size not in ['s', 'm', 'l']: 
    size = input("Pelase, tyoe a valid text. Sizes [S, M, L]:_ ").lower().strip()
if size in ['s', 'm', 'l']: 
    if size == 's': 
        price += 15
        if cheese == 'y': 
            price += 1
        if pepperoni == 'y':
            price += 2 
    
    elif size == 'm':
        price += 20
        if pepperoni == 'y':
            price += 3

    elif size == 'l':
        price += 25
        if pepperoni == 'y':
            price +=3

print(f'Here you are. The total price is: ${price}')


