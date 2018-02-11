class playerClass():

    #holds information related to the character
    def __init__(character,name,age):

        #sets the characters name and age
        character.name = name
        character.age = age

    def abilityScores(attribute,strength,craft,charisma):

        attribute.strength = strength
        attribute.craft = craft
        attribute.charisma = charisma

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

        


    
