print('Welcome to Treasure Island Game!\n'
      'Your mission is to find the treasure\n')

choice_1 = input("You're at a cross road. Wher you want to go?" ' Type "left"or "right":\n').lower().strip()
    
if choice_1 in ['left', 'right']:
    if choice_1 == 'right':
        status = 'lose'
    else:

        choice_2 = input('You come to a lake. Ther is an island in the midle of the lakke. Type wait to wait for a boat. Type swim to swim across. \n').strip().lower()
        if choice_2 in ['swim', 'wait']:
            if choice_2 == 'swim':
                status = 'lose'
            else:
                choice_3 = input('You arrive at the island unharmed. There is a house with 3 doors. One, red, one yellhow and one blue. Which color do you chose?\n').strip().lower()
                if choice_3 in ['red', 'blue', 'yellow']:
                    if choice_3 in ['red', 'blue']:
                        status = 'lose'
                    else:
                        status = 'win'
                if choice_3 not in ['red', 'blue', 'yellow']:
                    print('You typed incorrectly. Game Over')                
        if choice_2 not in ['swim', 'wait']:
            print('You typed incorrectly. Game Over') 
if choice_1 not in ['left', 'right']: 
    print('You typed incorrectly. Game Over') 
if status == 'lose':
    print('Sorry you died. Game over. ')
elif status == 'win':
    print("Congratulations! You found the Treasure!!")