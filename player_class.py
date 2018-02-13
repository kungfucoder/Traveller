class playerClass():

    #holds information related to the character
    def __init__(character,name,age):

        #sets the characters name and age
        character.name = name
        character.age = age

        print('Hello, ' + name.title() + ' good to meet you.')
        
    def abilityScores(attribute,strength,craft,charisma):

        attribute.strength = str(strength)
        attribute.craft = str(craft)
        attribute.charisma = str(charisma)

        print('Your strength is, ' + strength + '.')
        print('Your craft is, ' + craft + '.')
        print('Your charisma is, ' + charisma + '.')


       def intimidate(self):
        return (self.strength - 10) / 2
        

    def lift(self):
        return (self.strength - 10) / 2

    def climb(self):
        return (self.strength - 10) / 2

    def repair(self):
        return (self.craft - 10) / 2

    def build(self):
        return (self.craft - 10) / 2

    def appraise(self):
        return (self.craft - 10) / 2

    def persuade(self):
        return (self.charisma - 10) / 2

    def deceive(self):
        return (self.charisma - 10) / 2

    def rally(self):
        return (self.charisma - 10) / 2

attrs1 = {
    "name": "James",
    "age": 24,
    "strength": 12,
    "craft": 16,
    "charisma": 13
}

attrs2 = {
    "name": "Matthew",
    "age": 36,
    "strength": 14,
    "craft": 11,
    "charisma": 16
}

player1 = playerClass(attrs1)
player2 = playerClass(attrs2)

player1.abilityScores()
print player1.intimidate()
print player1.lift()
print player1.climb()

player2.abilityScores()
print player2.intimidate()
print player2.lift()
print player2.climb()
