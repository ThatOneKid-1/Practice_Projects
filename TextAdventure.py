import sys

def Adv_Start():

    #enter start for answer
    Answer=input("new game\ntype start:\n")    
    if Answer == "start":
        print("Welcome to the start of your adventure")
    elif Answer != "start":
        sys.exit("INVALID RESPONSE\nYou did not start the game")

def Adv():
    #start of path choices
    Answer=input("You enter a cave and find a sword do you take it?\nYes or No?\n")
    if Answer == "Yes":
        print("you picked up the sword and continued through the cave")
    elif Answer == "No": 
        print("You left the sword and continued through the cave")
    else: 
        sys.exit("INVALID RESPONSE\ntry again and give a valid response")

    Ans=input("You encounter a dragon, what do you do?\nRUN, fight it, try to befriend it, or give up\n")
    if Ans == "RUN":
        print("You ran away and hid from the dragon succesfully")
        print('You then continue running after a few minutes and find yourself in a nearby town.\nThe townsfolk tell you about a dragon thats been terrorizing them.\nYou explain to them that you saw the dragon and ran from it and that it may have followed you.')
        Ans2=input('The dragon appears in the town and the townsfolk are terrified and ask for your help. What do you do?\nfight it, or give up\n')
        if Ans2 == 'fight it':
            if Answer == 'Yes':
                sys.exit('You fight the dragon with your sword and slay it after a long battle.\nYou saved the town')
            elif Ans2 == 'fight it':
                if Answer == 'No':
                    sys.exit('You get a sword from one of the townsfolk and slay the dragon after a long battle\nYou saved the town')
        elif Ans2 == 'give up':
            sys.exit('You give up and the dragon brutally kills you and destroys the town.\nGAME OVER')
    elif Ans == "try to befriend it":
        sys.exit("The dragon was starting to get calm and was then spooked by a branch it broke by stepping on...\nIt then killed you\nGAME OVER")
    elif Ans == "give up":
        sys.exit("The dragon gives you mercy and tries to kill you in the quickest way it can.\nThe dragon bites your head off and then eats it... it later eats the rest of you\nGAME OVER")
    elif Ans == "fight it":
        if Answer == "Yes":
            print("you fought the dragon with your sword and after a long battle you slayed it.")
            print('You then continue your journey and arrive at a nearby town.\nOnce at the town the townsfolk tell you about a dragon thats been terrrorizing them.\nYou then explain to them that you just slayed the dragon and that they\'re safe now.')
            sys.exit('You have gotten the good ending')
        elif Ans == "fight it":
            if Answer == "No":
                sys.exit("You tried to fight it without a sword and died\nGAME OVER")
    else:
        sys.exit("INVALID RESPONSE\nTry again and give a valid response")

Adv_Start()
Adv()