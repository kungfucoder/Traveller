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


        def strengthSkills(bonus,intimidate,lift,climb):

            bonus.intimidate = intimidate
            bonus.lift = lift
            bonus.climb = climb

        def craftSkills(bonus,appraise,repair,build):

            bonus.appraise = appraise
            bonus.repair = repair
            bonus.build = build

        def charismaSkills(bonus,persuade,deceive,rally):

            bonus.persuade = persuade
            bonus.deceive = deceive
            bonus.rally = rally


        myAttributes = abilityScores(12,16,13)

myCharacter = playerClass('James', 24)
