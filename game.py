import random

state = 0


def investigate():
    global state


class Stage():
    def __init__(self, newType):
        #self.levelTypes refers to a variable inside of the Level Object
        self.newType = newType  
    def levelPrints(self):
        print(self.newType)


#List of game levels
setStage = []
#At this point we have an empty list container

#This creates list of dungeons and adds them to level
for i in range(2):
    #Create an empty container to hold our level types
    randomLType = [] #going to include 3 numbers
    #Generates 3 Random level types
    for x in range(3):
        randomLType.append(random.randint(0,2)) # generates 0,1,2 and add to randomLType
    #Once loop is done, randomLType now contains 3 numbers corresponding to dungeons types
    #print(randomLType)
    #every time main loop runs we create a new object
    #giving information from randomLtype to a Level object
    temp = Stage(randomLType)
    #temp becomes a Level object
    #add temp to setLevels list
    setStage.append(temp)

#print(setLevels)
print("Original Stages...")

#levelPrints is a function of the Level object
#Here i is looping through objects
for levelObject in setStage:
    #i = current Level object
    levelObject.levelPrints()

print("Setting Boss Stage...")

#len is length, size of list, size of setLevels is 10
#i is looping through range numbers
for number in range(len(setStage)):
    #i = index
    if (number == 5 or number == 9):
        #setting a boss condition
        #setLevels[i].levelTypes refers to the variable levelTypes inside of the object
        setStage[number].newType = [3,3,3]
    setStage[number].levelPrints()


    if (state == 0):
        print("you are looking for someone that has been missing for over a few weeks you got a call and decided that maybe some possible leads can be found in the place of the inicident.")
        print("you find out where the shelter is and decide to head there first.")
        command = input("where do you want to go?")
            if (command == "shelter")
            state = 1
            else :
                print ("I should go to the shelter first")
                state = 0

    if (state == 1):     
        print("You come to a house that has been used sort of as a shelter for  abandonded and homeless children")
        print ("you figure this would be a good first stop to find out more information as to her whereabouts")

        command = input("investigate, ask around, keep moving ")
        if (command == "investigate"):
            subCommand = input("return or search")
            if (subCommand == "search")
                print("You find a crumbled note in the trash.")
                print(" It says ' if you're reading this, I'm already gone. dont look for me, \n J' ")
            elif (subCommand == "return")
                print("You return to the entrance")
                command = input("investigate, ask around, keep moving ")
        elif(command == "ask around"):
            subCommand = input("ask owner, question the little girl in the corner, question guard by the lobby")
                if (subCommand == "ask owner")
                    print("Y ou have a chat with the owner")
                elif (subCommand == "question the little girl in the corner")

                elif (subCommand == "question the guard")



        elif(command == "keep moving")
        state = 2
        # beginning of game
    # the story goes that you are looking for a child said t be missing for a few weeks
    #
    #you find a letter she wrote to parents saying she is planning on leaving town in the next few days and tht she has found someone that promised her a normal life, a man named Hue.
    # second lvl
    # you come across a tractor truck headed toward the outskirts of the city you have heard rumors that these trucks are used to trasport children outside the city where they are used as labor works by Hue

