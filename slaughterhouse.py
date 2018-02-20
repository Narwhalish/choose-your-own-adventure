"""
Name: Emily Liu
Choose Your Own Adventure
Billy Pilgrim's Adventure Through Time

Slaughterhouse Room (Need Certain Number of Items)
In the slaughterhouse there are:
    Guards - Learn more about the room, get clues on how to leave, on Vonnegut
    Syrup - Boosts HP
    Spoon - Must have to eat syrup
    Other Americans - Learn more about the game, more clues about Vonnegut
    Shrapnel - Loses HP 
    Shovel - Key to leave the room 
    
** User Notes: Type %matplotlib inline in the kernel before playing game
                All user entries are case-insensitive**
================================================================================
"""
import matplotlib.pyplot as plt

global space, position
space = [[0]*5 for i in range(5)]
global f_shovel, f_spoon
f_shovel=False
f_spoon=False

space[4][2]="Entrance"
space[0][1]="Guards"
space[0][3]="Door"
space[3][3]="Americans"
space[1][4]="Syrup"
entrancepos=[4,2]
doorpos = [0,3]
guardpos = [0, 1]
syruppos = [1, 4]
spoonpos = [4, 0]
amerpos = [3, 3]
shrapnelpos = [2, 1]
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

def action():
    global prow, pcolumn, space, position
    a = raw_input('Up, Down, Right, Left (U,D,R,L): ').upper()
    if ( a == 'U'):
        space[prow][pcolumn]=0
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
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 
    if (a =='D'):
        space[prow][pcolumn]=0
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
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 
    if (a =='L'):
        space[prow][pcolumn]=0
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
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 
    if (a =='R'):
        space[prow][pcolumn]=0
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
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 

def entrance():
    space[doorpos[0]][doorpos[1]]="YOU\nDoor"
    make_map()
    print "Do you want to leave the slaughterhouse?"
    d = (raw_input("To leave, press L. To stay, press S: ")).upper()
    if (d =='L'):
        pass #leads to last room 
    elif (d == 'S'):
        print "You decided to stay in the slaughterhouse."
        print "Maybe there are more items!"
        action()

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
            a=False
        elif (d == 'S'):
            print "You decided to stay in the slaughterhouse."
            print "Maybe there are more items!"
            a=False
            action()
        else:
            print "\nPlease enter a valid action!\n"

def guards():
    a = True
    b = True
    space[doorpos[0]][doorpos[1]]="YOU\nGuards"
    make_map()
    print "You found three guards!"
    while (a):
        print "Maybe they have information. Will you talk to them?"
        d = (raw_input("To talk, press T. To ignore, press I: ")).upper()
        if (d =='T'):
            print "One of the guards sees and turns to you."
            a=False
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
                    b = False
                    action()
                elif (a=='B'):
                    print "GUARD: You flamingo! You're in the underground Slaughterhouse.\
                            \nIf you weren't, you'd be dead by now."
                    b = False
                    action()
                elif (a=='C'):
                    print "GUARD: It gives you energy and raises your HP."
                    b=False
                    action()
                elif (a=='D'):
                    print "GUARD: Find Kurt Vonnegut and save us. He is the master of this\
                            \ngame and the one who made us suffer through Dresden."
                    b=False
                    action()
                else:
                    print "\nPlease enter a valid answer!\n"
        elif (d == 'I'):
            print "You decided to ignore the guards."
            a=False
            action()
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
                a = False
                pass #boost HP
            elif (d=='L'):
                print "You decided not to drink the syrup."
                a = False
            else:
                print "\nPlease enter a valid action!\n"
    else:
        print "You don't have the means to drink the syrup!"
            
    
def spoon():
    global f_spoon
    f_spoon=True
    print "You found a spoon!"
    print "Perhaps you can use it to eat something."
    space[spoonpos[0]][spoonpos[1]]="Spoon"
    make_map()

def americans():
    print "You found your fellow Americans!"
    space[amerpos[0]][amerpos[1]]="Americans"
    make_map()

def shrapnel():
    print "You found shrapnel!"
    space[shrapnelpos[0]][shrapnelpos[1]]="Shrapnel"
    make_map()
    print "Oh no! You stepped on the shrapnel and lost HP!"
    #lose HP function

def shovel():
    global f_shovel
    f_shovel=True
    print "You found a shovel!"
    print "Maybe the guards will let you leave if you help them bury the bodies?"
    space[shovelpos[0]][shovelpos[1]]="Shovel"
    make_map()
    
def items():
    decisions = {str(doorpos): door,
                str(guardpos): guards,
                str(syruppos): syrup,
                str(spoonpos): spoon,
                str(amerpos): americans,
                str(shrapnelpos): shrapnel,
                str(shovelpos): shovel,
                str(entrancepos): entrancepos}
    decisions[str(position)]()
    
def main():
    print "\n You have discovered the Slaughterhouse!"
    
    global space, door, position
    space[prow][pcolumn]=x
    make_map()
    
    while (found_door==False):
        action()
    
    
if __name__ == '__main__':
    main()