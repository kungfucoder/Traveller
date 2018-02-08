#sets the path for the character to go

import random

roll = random.randint(1, 20)

strength = 10

craft = 10

charisma = 10

def virtualDie(roll):
    roll = random.randint(1,20)
    roll = str(roll)
    print('You rolled, ' + roll + '.')
    roll = int(roll)
    
     return;

print('Hello Traveller! What is your name?')

name = input()

print('Great to meet you, ' + name + ', I am your guide.')

print('I will present you with choices, the decisions of which will decide your fate on this journey.')

print('Before you travel any further, I will bestow upon you a gift.')

print('this will be the first of many choices you will have to make.')

print('There are three main attributes that help people get by in this world, strength, craft and, charisma.')

print('I will give yout he ability to boost these attributes as you see fit until my gift has been depleted.')

print('Your base number is 10 for each ability. My gift is 7 points to distribute among the three abilities. Choose wisely')

giftedStats = 0
print('Which ability do you wish to raise?')

print('strength, craft, or charisma? Enter \'1\' for strength, \'2\' for craft and, \'3\' for charisma')

for giftedStats in range(7):
     choice = input(['1', '2', '3'])

     if choice == '1':
          strength = strength + 1
          print('Your strength is now')
          print(strength)

     elif choice == '2':
          craft = craft + 1 
          print('Your craft is now')
          print(craft)
     elif choice == '3':
          charisma = charisma + 1 
          print('Your charisma is now')
          print(charisma)
     if giftedStats > 6:
          break 

print('Wise choices!')
