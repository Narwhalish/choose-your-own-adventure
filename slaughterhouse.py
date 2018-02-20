"""
Name: Emily Liu
Choose Your Own Adventure
Billy Pilgrim's Adventure Through Time

Slaughterhouse Room (Need Certain Number of Items)
In the slaughterhouse there are:
    Guards
    Syrup - Boosts HP
    Spoon - Must have to eat syrup
    Other Americans
    Shrapnel
    Shovel - Key to leave the room 
    
** User Notes: Type %matplotlib inline in the kernel before playing game
                All user entries are case-insensitive**
================================================================================
"""
import matplotlib.pyplot as plt

global space, position
space = [[0]*5 for i in range(5)]

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
    space[doorpos[0]][doorpos[1]]="YOU\nDoor"
    make_map()
    print "You found a door!"
    print "I wonder where this door leads... Will you open the door?"
    d = (raw_input("To enter, press E. To stay, press S: ")).upper()
    if (d =='E'):
        pass #leads to new room 
    elif (d == 'S'):
        print "You decided to stay in the slaughterhouse."
        print "Maybe there are more items!"
        action()
def guards():
    space[doorpos[0]][doorpos[1]]="YOU\nGuards"
    make_map()
    print "You found three guards!"
    print "Maybe they have information. Will you talk to them?"
    d = (raw_input("To talk, press T. To ignore, press I: ")).upper()
    if (d =='T'):
        print "One of the guards sees and turns to you."
        print "'Stay inside! Dresden is being bombed.'"
        a = (raw_input("a. 'How can I leave?'\n \
                        b. 'What's the syrup for?' \n \
                        c. '
    elif (d == 'I'):
        print "You decided to ignore the guards."
        action()
    
def syrup():
    print "You found a bottle of syrup!"
    space[syruppos[0]][syruppos[1]]="Syrup"
    make_map()
def spoon():
    print "You found a spoon!"
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
def shovel():
    print "You found a shovel!"
    space[shovelpos[0]][shovelpos[1]]="Shovel"
    make_map()
    
def items():
    decisions = {str(doorpos): door,
                str(guardpos): guards,
                str(syruppos): syrup,
                str(spoonpos): spoon,
                str(amerpos): americans,
                str(shrapnelpos): shrapnel
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