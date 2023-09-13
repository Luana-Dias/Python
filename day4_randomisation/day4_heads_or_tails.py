
import random 

print("Hello!! Let's play heads or tails!")

player_choice = input('Choose your bet. [H or T]:_ ').upper(). strip()
coin = ['H', 'T']
coin_side = random.choice(coin)

if player_choice == coin_side:
    print("You Won! ")
if player_choice != coin_side:
    print("Sorry. You lost.")