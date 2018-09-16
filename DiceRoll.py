import random
while 1:
    whole = 0
    rawText = input('Type the # of sides on the die to roll and press Enter:')
    try: 
        dieSides = int(rawText)
    except ValueError:
        print('Hey! Thats not a whole number!')
    else:
        print("Rolling a '" + str(dieSides) + "' sided die!")
        print(random.randint(1,dieSides))