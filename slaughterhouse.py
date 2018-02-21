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

global space, position
space = [[" "]*5 for i in range(5)]
global f_shovel, f_spoon
f_shovel=False
f_spoon=False

space[0][1]="Guards"
#space[0][3]="Door"
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

global prow, pcolumn, position
prow = 4
pcolumn = 2
x = "YOU"
position = [prow, pcolumn]

global door
found_door = False

def print_space():
    global space
    for row in space:
        print row
        print '\n'

def make_map():
    global space, position
    #print_space()
        
    print "\n MAP OF SLAUGHTERHOUSE"
    color_grid = [['black']*5 for i in range(5)]
    
    pmap = plt.table(cellText=space, cellColours=color_grid,
            cellLoc='center', rowLoc='left', colLoc = 'center',
            loc='center', bbox=None)

    pmap.scale(1, 3.65)
    plt.xticks([])
    plt.yticks([])
    table_cells = pmap.properties()['child_artists']
    
    for cell in table_cells:
        cell._text.set_color('white')
        cell.set_edgecolor('white')
    
    plt.show()

def check_continue():
    c = (raw_input("Press C to continue: ")).upper()
    a = True
    while (a):
        if (c=='C'):
            a = False
            return
        else: 
            print "Please press C." 

def action():
    global prow, pcolumn, space, position
    a = raw_input('Up, Down, Right, Left (U,D,R,L): ').upper()
    if ( a == 'U'):
        space[prow][pcolumn]=" "
        if prow!=0:
            prow=prow-1
            position = [prow, pcolumn]
            #print "Position = " + str(position)
            space[position[0]][position[1]]=x
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or 
                position==shovelpos or position==entrancepos):
                items()
            else:
                space[4][2]="Entrance"
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 
    if (a =='D'):
        space[prow][pcolumn]=" "
        if prow!=4:
            prow=prow+1
            position = [prow, pcolumn]
            #print "Position = " + str(position)
            space[position[0]][position[1]]=x
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or 
                position==shovelpos or position==entrancepos):
                items()
            else:
                space[4][2]="Entrance"
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 
    if (a =='L'):
        space[prow][pcolumn]=" "
        if pcolumn!=0:
            pcolumn=pcolumn-1
            position = [prow, pcolumn]
            #print "Position = " + str(position)
            space[position[0]][position[1]]=x
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or
                position==shovelpos or position==entrancepos):
                items()
            else:
                space[4][2]="Entrance"
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 
    if (a =='R'):
        space[prow][pcolumn]=" "
        if pcolumn!=4:
            pcolumn=pcolumn+1
            position = [prow, pcolumn]
            #print "Position = " + str(position)
            space[position[0]][position[1]]=x
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos or 
                position==shovelpos or position==entrancepos):
                items()
            else:
                space[4][2]="Entrance"
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 

def entrance():
    a = True
    space[entrancepos[0]][entrancepos[1]]="YOU\nEntrance"
    make_map()
    while (a):
        print "Do you want to leave the slaughterhouse?"
        d = (raw_input("To leave, press L. To stay, press S: ")).upper()
        if (d =='L'):
            pass #leads to last room 
            break
        elif (d == 'S'):
            print "You decided to stay in the slaughterhouse."
            print "Maybe there are more items!"
            break
        else:
            print "\nPlease enter a valid action!\n"

def door():
    global f_shovel
    a = True
    space[doorpos[0]][doorpos[1]]="YOU\nDoor"
    make_map()
    print "You found a door!"
    while (a):
        print "I wonder where this door leads... Will you open the door?"
        d = (raw_input("To enter, press E. To stay, press S: ")).upper()
        if (d =='E'):
            if (f_shovel):
                pass #leads to new room
            else: 
                print "Oops! You don't have the key to unlock this door!"
            break
        elif (d == 'S'):
            print "You decided to stay in the slaughterhouse."
            print "Maybe there are more items!"
            break
        else:
            print "\nPlease enter a valid action!\n"

def guards():
    a = True
    b = True
    space[guardpos[0]][guardpos[1]]="YOU\nGuards"
    make_map()
    print "You found three guards!"
    while (a):
        print "Maybe they have information. Will you talk to them?"
        d = (raw_input("To talk, press T. To ignore, press I: ")).upper()
        if (d =='T'):
            print "One of the guards sees and turns to you."
            a = False
            while (b):
                print "GUARD: Stay inside! Dresden is being bombed."
                a = (raw_input("a. 'How can I leave?'\
                                \nb. 'Where am I?' \
                                \nc. 'What's syrup for?'\
                                \nd. 'Tell me more about the game.'")).upper()
                if (a=='A'):
                    print "GUARD: You cannot leave without our permission!"
                    print "GUARD: There are a lot of dead bodies around and we need\
                            \nall the help we can get to shovel them."
                    break
                elif (a=='B'):
                    print "GUARD: You flamingo! You're in the underground Slaughterhouse.\
                            \nIf you weren't, you'd be dead by now."
                    break
                elif (a=='C'):
                    print "GUARD: It gives you energy and raises your HP."
                    break
                elif (a=='D'):
                    print "GUARD: Find Kurt Vonnegut and save us. He is the master of this\
                            \ngame and the one who made us suffer through Dresden."
                    break
                else:
                    print "\nPlease enter a valid answer!\n"
            break
        elif (d == 'I'):
            print "You decided to ignore the guards."
            break
        else:
            print "\nPlease enter a valid action!\n"

    
def syrup():
    global f_spoon
    a = True
    print "You found a bottle of syrup!"
    space[syruppos[0]][syruppos[1]]="YOU\nSyrup"
    make_map()
    if (f_spoon):
        print "Use the spoon to drink the syrup and boost your HP!"
        while (a):
            d = (raw_input("To drink, press 'D'. To leave, press 'L': ")).upper()
            if (d=='D'):
                break
                pass #boost HP
            elif (d=='L'):
                print "You decided not to drink the syrup."
                break
            else:
                print "\nPlease enter a valid action!\n"
    else:
        print "You don't have the means to drink the syrup!"
            
    
def spoon():
    a = True
    global f_spoon
    f_spoon=True
    print "You found a spoon!"
    print "Perhaps you can use it to eat something."
    space[spoonpos[0]][spoonpos[1]]="YOU\nSpoon"
    while (a):
        d = (raw_input("Do you want to put it in your backpack? Y or N: ")).upper()
        if (d=='Y'):
            break
            pass #put in backpack
        elif (d=='N'):
            break
            print "You left the spoon on the floor. It wasn't sanitary anyway."
        else: 
            print "\nPlease enter a valid action!\n"
    make_map()
    space[spoonpos[0]][spoonpos[1]]="Spoon"

def americans():
    a = True
    print "You found your fellow Americans!"
    space[amerpos[0]][amerpos[1]]="YOU\nAmericans"
    make_map()
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
        if (d=='A'):
            print "\nThe American squints at you. The dim lighting in the slaughterhouse seems\
                    \nto have gotten to his eyesight."
            print "He says gruffly, \"Yeah, we spoke to the guards... They don't want to let \
                    \nus out though. I don't know when they will.\" He turns back around, ending \
                    \nthe conversation."
            break
        elif (d=='B'):
            print "\n\"I don't know. We spoke to the guards an they don't want to let us leave. We're\
                    \nsurviving on syrup, but I think we'll die pretty soon. There's only enough syrup\
                    \nto go around for so long. I wish I told my wife goodbye.\""
            break
        elif (d=='C'):
            print "\nHe looks dazed by your question. \"Clocks? What clocks? All I know is that there is \
                    \nsomeone suspicious the guards were talking about... someone outside of here. But they \
                    \nwon't let us out, so I'm not going to worry about it.\""
            print "This could be useful, you thought. \"Did they say where?\""
            print "\"I think they mentioned something about a wagon.\" He turned around, \
                    \nfocusing on this syrup."
            break
        elif (d=='D'):
            break
        else:
            print "\nPlease print a valid answer!\n"
    

def shrapnel():
    print "You found shrapnel!"
    space[shrapnelpos[0]][shrapnelpos[1]]="Shrapnel"
    make_map()
    print "Oh no! You stepped on the shrapnel and lost HP!"
    #lose HP function

def shovel():
    global f_shovel
    f_shovel=True
    a=True
    space[shovelpos[0]][shovelpos[1]]="YOU\nShovel"
    make_map()
    space[shovelpos[0]][shovelpos[1]]="Shovel"
    print "You found a shovel!"
    print "Maybe the guards will let you leave if you help them bury the bodies?"
    while (a):
        d = (raw_input("\nDo you want to put it in your backpack? Y or N: ")).upper()
        if (d=='Y'):
            pass #backpack function
            break
        elif (d=='N'):
            print "You left the shovel. It seems like a dangerous object."
            break
        else:
            print "\nPlease enter a valid action!\n"

def items():
    decisions = {str(doorpos): door,
                str(guardpos): guards,
                str(syruppos): syrup,
                str(spoonpos): spoon,
                str(amerpos): americans,
                str(shrapnelpos): shrapnel,
                str(shovelpos): shovel,
                str(entrancepos): entrance}
    decisions[str(position)]()
    
def main():
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
    space[prow][pcolumn]=x
    make_map()
    
    while (found_door==False):
        action()
    
    
if __name__ == '__main__':
    main()