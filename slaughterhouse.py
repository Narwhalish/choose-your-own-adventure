"""
Name: Emily Liu
Choose Your Own Adventure
Billy Pilgrim's Adventure Through Time

Slaughterhouse Room (Need Certain Number of Items)
Goal: 
    Leave the room! 
In the slaughterhouse there are:
    Guards - Learn more about the room, get clues on how to leave, on Vonnegut
    Syrup - Boosts HP
    Spoon - Must have to eat syrup
    Other Americans - Learn more about the game, more clues about Vonnegut
    Shrapnel - Loses HP 
    Shovel - Key to leave the room, must reach certain HP to use shovel
    Door - only visible when shovel is found
    
** User Notes: Type %matplotlib inline in the kernel before playing game
                All user entries are case-insensitive**
================================================================================
"""
import matplotlib.pyplot as plt
import boss_battle
import zoo
import backpack
import matplotlib.image as mpimg

global space, position
space = [[" "]*5 for i in range(5)]

space[4][2]="Entrance"
space[0][1]="Guards"
space[3][3]="Americans"
space[1][4]="Syrup"
entrancepos=[4,2]
doorpos = [0,3]
guardpos = [0,1]
syruppos = [1,4]
spoonpos = [4,0]
amerpos = [3,3]
shrapnelpos = [2,1]
shovelpos = [2,2]
adithyapos = [0,4]

global prow, pcolumn, position
prow = 4
pcolumn = 2
x = "YOU"
position = [prow, pcolumn]

def displayImage(name):
    image = mpimg.imread(name)
    ax = plt.axes(frameon=False)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(image)
    plt.show()
    
def make_map():
    global space, position
        
    print "\n MAP OF SLAUGHTERHOUSE"
    color_grid = [['black']*5 for i in range(5)] #makes all of the grids spaces black
    
    pmap = plt.table(cellText=space, cellColours=color_grid, #formats the table on matplotlib
            cellLoc='center', rowLoc='left', colLoc = 'center',
            loc='center', bbox=None)

    pmap.scale(1, 3.65)
    plt.xticks([])
    plt.yticks([])
    table_cells = pmap.properties()['child_artists']
    
    for cell in table_cells:
        cell._text.set_color('white')
        cell.set_edgecolor('white')
    
    plt.show() #displays the map
    print "HP: " + str(hp) + " / 150" #prints out the HP of the user

def check_continue(): #allows user to delay narration
    a = True
    while (a):
        c = (raw_input("Press C to continue: ")).upper()
        if (c=='C'):
            a = False
            break
        else: 
            print "Please press C." 

def action(): #allows user to move around on the map or print backpack
    global prow, pcolumn, space, position, bp
    a = raw_input('Up, Down, Right, Left, Backpack (U,D,R,L,B): ').upper()
    if ( a == 'U'): #if user chooses to go up 
        if prow!=0: #prevents user from going off map
            prow=prow-1
            position = [prow, pcolumn]
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or 
                position==shovelpos or position==entrancepos or 
                position==adithyapos):
                #if user happens to land on one of the positions with an item
                items() #redirects to various other functions
            else:
                space[position[0]][position[1]]=x #makes position say "YOU"
                make_map()
                space[prow][pcolumn]=" " #resets position
        else:
            print "You can't walk through a wall!"
            action() 
    elif (a =='D'): #if user wants to move down
        if prow!=4:
            prow=prow+1
            position = [prow, pcolumn]
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or 
                position==shovelpos or position==entrancepos or
                position==adithyapos):
                items()
            else:
                space[position[0]][position[1]]=x
                make_map()
                space[prow][pcolumn]=" "
        else:
            print "You can't walk through a wall!"
            action() 
    elif (a =='L'): #if user wants to move left
        if pcolumn!=0:
            pcolumn=pcolumn-1
            position = [prow, pcolumn]
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or
                position==shovelpos or position==entrancepos or 
                position==adithyapos):
                items()
            else:
                space[position[0]][position[1]]=x
                make_map()
                space[prow][pcolumn]=" "

        else:
            print "You can't walk through a wall!"
            action() 
    elif (a =='R'): #if user wants to move right
        if pcolumn!=4:
            pcolumn=pcolumn+1
            position = [prow, pcolumn]
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or 
                position==shovelpos or position==entrancepos or
                position==adithyapos):
                items()
            else:
                space[position[0]][position[1]]=x
                make_map()
                space[prow][pcolumn]=" "
        else:
            print "You can't walk through a wall!"
            action() 
    elif (a=='B'): #if user wants to view backpack
       bp, hp = backpack.main(bp, hp) #call function to print backpack contents
       action() 
    else: 
        print "Please enter a valid action!"
        action()

def entrance(): #if user lands on entrance position, allows user to go back to last room
    a = True
    space[entrancepos[0]][entrancepos[1]]="YOU\nEntrance"
    make_map()
    space[entrancepos[0]][entrancepos[1]]="Entrance"
    while (a):
        print "Do you want to leave the slaughterhouse?"
        d = (raw_input("To leave, press L. To stay, press S: ")).upper()
        if (d =='L'):
            zoo.main(bp, hp, eggs) #leads to last room, zoo
        elif (d == 'S'):
            print "You decided to stay in the slaughterhouse."
            print "Maybe there are more items!"
            return
        else:
            print "\nPlease enter a valid action!\n"

def door(): #if user lands on door position, allows user to move to next room if shovel is found
    a = True
    space[doorpos[0]][doorpos[1]]="YOU\nDoor"
    make_map()
    space[doorpos[0]][doorpos[1]]="Door"
    print "You found a door!"
    while (a): 
        print "I wonder where this door leads... Will you open the door?"
        d = (raw_input("To enter, press E. To stay, press S: ")).upper()
        if (d =='E'):
            if ('shovel' in bp): #if user has a shovel
                boss_battle.narrate(eggs) #leads to next room, the boss battle
            else: #if user doesn't have a shovel
                print "Oops! You don't have the key to unlock this door!"
            break
        elif (d == 'S'): 
            print "You decided to stay in the slaughterhouse."
            print "Maybe there are more items!"
            return
        else:
            print "\nPlease enter a valid action!\n"

def guards(): #if user lands on guards position, can talk to guards for hints
    a = True
    b = True
    space[guardpos[0]][guardpos[1]]="YOU\nGuards"
    make_map()
    space[guardpos[0]][guardpos[1]]="Guards"
    print "You found three guards!"
    while (a):
        print "Maybe they have information. Will you talk to them?"
        d = (raw_input("To talk, press T. To ignore, press I: ")).upper()
        if (d =='T'): #if user talks to guards
            print "One of the guards sees and turns to you."
            a = False #so that loop doesn't keep looping
            while (b):
                print "GUARD: Stay inside! Dresden was bombed. You can't leave without our persmission!." 
                a = (raw_input("a. 'How can I leave?'\
                                \nb. 'Where am I?' \
                                \nc. 'What's syrup for?'\
                                \nd. 'Tell me more about the game.'")).upper()
                if (a=='A'): #guard gives hint about key
                    print "GUARD: You cannot leave without our permission!"
                    print "GUARD: There are a lot of dead bodies around and we need\
                            \nall the help we can get to shovel them."
                    break
                elif (a=='B'): #guard tells user room
                    print "GUARD: You flamingo! You're in the underground Slaughterhouse.\
                            \nIf you weren't, you'd be dead by now."
                    break
                elif (a=='C'): #guard informs about syrup
                    print "GUARD: It gives you energy and raises your HP."
                    break
                elif (a=='D'): #guard gives hint about the clock master
                    print "GUARD: Find the clockmaster outside and save us. He is the master of this\
                            \ngame and the one who made us suffer through Dresden."
                    break
                else:
                    print "\nPlease enter a valid answer!\n"
            break
        elif (d == 'I'): #if user doesn't talk to guards
            print "You decided to ignore the guards."
            break
        else:
            print "\nPlease enter a valid action!\n"

    
def syrup(): #if user lands on syrup position, can drink to raise HP by 25 points
    global hp
    a = True
    print "You found a bottle of syrup!" 
    space[syruppos[0]][syruppos[1]]="YOU\nSyrup"
    make_map()
    space[syruppos[0]][syruppos[1]]="Syrup"
    if ('spoon' in bp): #can only drink syrup if user has a spoon in backpack
        print "Use the spoon to drink the syrup and boost your HP!"
        while (a):
            d = (raw_input("To drink, press 'D'. To leave, press 'L': ")).upper()
            if (d=='D'): #if user drinks 
                break
                hp+=25 #boost HP
            elif (d=='L'): #if user doesn't drink
                print "You decided not to drink the syrup."
                break
            else:
                print "\nPlease enter a valid action!\n"
    else:
        print "You don't have the means to drink the syrup!"
            
    
def spoon(): #if user lands on spoon position, can put in backpack
    a = True
    if ('spoon' not in bp): #if the user doesn't already have a spoon
        space[spoonpos[0]][spoonpos[1]]="YOU\nSpoon"
        make_map()
        print "You found a spoon!"
        print "Perhaps you can use it to eat something."
        while (a):
            d = (raw_input("Do you want to put it in your backpack? Y or N: ")).upper()
            if (d=='Y'):
                bp.append('spoon') #put in backpack
                space[spoonpos[0]][spoonpos[1]]=" "
                return
            elif (d=='N'): #if user doesn't want spoon
                print "You left the spoon on the floor. It wasn't sanitary anyway."
                space[spoonpos[0]][spoonpos[1]]="Spoon"
                return
            else: 
                print "\nPlease enter a valid action!\n"
    else: #deletes spoon from map
        space[spoonpos[0]][spoonpos[1]]=x
        make_map()
        space[spoonpos[0]][spoonpos[1]]=" "


def americans(): #if user lands on americans position, can converse with them for hints
    a = True
    print "You found your fellow Americans!"
    space[amerpos[0]][amerpos[1]]="YOU\nAmericans"
    make_map()
    space[amerpos[0]][amerpos[1]]="Americans"
    print "\nFive Americans were standing in a group, huddled together and eating\
            \nsyrup. They ignore you when you go up to them."
    print "\"Where did you get the syrup?\" you ask, hoping to share in on their pleasure."
    print "\"It's somewhere in the slaughterhouse. You have to find it yourself.\""
    check_continue()
    print "Suddenly, one of the Americans turns and scrutinizes you, as if just realizing you \
            \nwere there. \"Do you need something?\""
    while (a):
        d = (raw_input("a. Have you spoken to the guards yet?\
                    \nb. How do I leave?\
                    \nc. Do you know who is messing with the clocks?\
                    \nd. Nevermind.\nAnswer: ")).upper()
        if (d=='A'): #gives hints about the guards
            print "\nThe American squints at you. The dim lighting in the slaughterhouse seems\
                    \nto have gotten to his eyesight."
            print "He says gruffly, \"Yeah, we spoke to the guards... They don't want to let \
                    \nus out though. I don't know when they will.\" He turns back around, ending \
                    \nthe conversation."
            break
        elif (d=='B'): #gives hints about the key to leave
            print "\n\"I don't know. We spoke to the guards an they don't want to let us leave. We're\
                    \nsurviving on syrup, but I think we'll die pretty soon. There's only enough syrup\
                    \nto go around for so long. I wish I told my wife goodbye.\""
            break
        elif (d=='C'): #gives hints about the clockmaster
            print "\nHe looks dazed by your question. \"Clocks? What clocks? All I know is that there is \
                    \nsomeone suspicious the guards were talking about... someone outside of here. But they \
                    \nwon't let us out, so I'm not going to worry about it.\""
            print "This could be useful, you thought. \"Did they say where?\""
            print "\"I think they mentioned something about a wagon.\" He turned around, \
                    \nfocusing on this syrup."
            break
        elif (d=='D'): #if user doesn't want to talk 
            break
        else:
            print "\nPlease print a valid answer!\n"
    

def shrapnel(): #if user steps on shrapnel, loses 50 HP
    global hp
    space[shrapnelpos[0]][shrapnelpos[1]]="YOU\nShrapnel"
    make_map()
    space[shrapnelpos[0]][shrapnelpos[1]]="Shrapnel"
    print "You found shrapnel!"
    print "Oh no! You stepped on the shrapnel and lost HP!"
    hp-=50 #decrease HP by 50 points

def shovel(): #if user lands on shovel position, can keep it in backpack as key to leave the room
    a=True
    if ('shovel' not in bp): #if shovel not already in backpack
        space[shovelpos[0]][shovelpos[1]]="YOU\nShovel"
        make_map()
        print "You found a shovel!"
        print "Maybe the guards will let you leave if you help them bury the bodies?"
        while (a):
            d = (raw_input("\nDo you want to put it in your backpack? Y or N: ")).upper()
            if (d=='Y'): #put shovel in backpack
                bp.append('shovel')
                space[shovelpos[0]][shovelpos[1]]=" "
                return
            elif (d=='N'): #leave shovel 
                print "You left the shovel. It seems like a dangerous object."
                space[shovelpos[0]][shovelpos[1]]="Shovel"
                return
            else:
                print "\nPlease enter a valid action!\n"
    else: #delete the shovel from the map
        space[shovelpos[0]][shovelpos[1]]=x
        make_map()
        space[shovelpos[0]][shovelpos[1]]=" "

def adithya(): #if the user finds Sally the ghost, can receive an easter egg from her
    a = True
    if ('slaughterhouseadithya' not in eggs): #if user has not already gotten the egg
        print "You have found Sally!" 
        print "\"Hello, Billy. My name is Sally. Although I am not mentioned in the book,\
                \nI was actually a ghost who lived in the corner of Slaughterhouse-Five.\""
        check_continue()
        print "You're confused, but you let her continue. \"I will give you one chance to \
                \nmake a difference in your fate. Answer this question:"
        while (a): #trivia question to receive the egg
            d = (raw_input("How tall is Adithya? \
                            \na. Adithya-short\
                            \nb. Short\
                            \nc. Tall\
                            \nd. Lebron James - tall\
                            \nAnswer: ")).upper()
            if (d == 'B'): #if user answers correctly
                print "Sally looks extremely ecstatic. \"Correct!\" she cheers. \"To award you for\
                        \nyour smartness, take this: "
                displayImage('adithya4.jpg') #displays image of egg
                print "It appears to be an Adithya. You don't know why, but you take it anyway."
                eggs.append('slaughterhouseadithya') #adds egg to easter egg list
                return
            if (d=='A' or d=='C' or d=='D'): #if user answers incorrectly 
                print "Sally looks disappointed. \"You could've done better. Baiyo.\" She floats away\
                        \ngloomily."
                return
            else:
                print "Please enter a valid answer!"
    else: #don't do anything about Sally. She does not appear on the list because she is a ghost.
        pass
            

def items(): #redirects users from action() to a specific position function
    decisions = {str(doorpos): door,
                str(guardpos): guards,
                str(syruppos): syrup,
                str(spoonpos): spoon,
                str(amerpos): americans,
                str(shrapnelpos): shrapnel,
                str(shovelpos): shovel,
                str(entrancepos): entrance,
                str(adithyapos): adithya}
    decisions[str(position)]()
 
def main(b, h, e): #backpack, HP, eggs from last room
    global bp, hp, eggs
    bp = b
    hp = h
    eggs = e
    print "\n****************************************************************\n"
    print "You blink once, twice. The lighting is dim, and your eyes have to adjust to \
            \nsee the items around you. There are guards in the corner, plus a huddle of \
            \npitiful looking Americans. Your fellow Americans, caught in World War II. \
            \nYour heart sank. You are in Dresden, 1945."
    check_continue()
    print "\n****************************************************************\n"
    print "The underground slaughterhouse was named Slaughterhouse-Five. Minutes after you \
            \nrealize where you are, you hear the thundering sounds of bombs as their shells \
            \ncrack open above the ceiling." 
    check_continue()
    print "\n****************************************************************\n"
    print "After hours of shelling, you look around for a door, but it's too dim to make out \
            \none. Time is spinning erratically now -- you can feel it. The clockmaster is \
            \nnear. Find a way out of the slaughterhouse to get to the clockmaster!"
    check_continue()
    print "\n****************************************************************\n"
    
    global space, door, position
    space[prow][pcolumn]=x #makes the first position "YOU"
    make_map()
    space[entrancepos[0]][entrancepos[1]]="Entrance"
    a=True #loops the action()
    
    while (a):
        action()
    
    
# if __name__ == '__main__':   (used for testing purposes)
#     main([], 150, [])