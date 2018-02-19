"""
Name: Emily Liu
Choose Your Own Adventure
Billy Pilgrim's Adventure Through Time

Slaughterhouse Room (Need Certain Number of Items)
In the slaughterhouse there are:
    Guards
    Syrup
    Spoon
    Other Americans
    Shrapnel
    
** User Notes: Type %matplotlib inline in the kernel before playing game **
================================================================================
"""
import matplotlib.pyplot as plt

global space, position
space = [[0]*5 for i in range(5)]

space[4][2]="Entrance"
doorpos = [0,3]
guardpos = [0, 1]
syruppos = [1, 4]
spoonpos = [4, 0]
amerpos = [3, 3]
shrapnelpos = [2, 1]

global prow, pcolumn, position
prow = 4
pcolumn = 2
x = "You"
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
    a = raw_input('Up, Down, Right, Left (U,D,R,L): ')
    if ( a == 'U'):
        space[prow][pcolumn]=0
        if prow!=0:
            prow=prow-1
            position = [prow, pcolumn]
            #print "Position = " + str(position)
            space[position[0]][position[1]]=x
            if (position==doorpos or position==guardpos or  
                position==syruppos or position==spoonpos or
                position==amerpos or position==shrapnelpos):
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
                position==amerpos or position==shrapnelpos):
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
                position==amerpos or position==shrapnelpos):
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
                position==amerpos or position==shrapnelpos):
                items()
            else:
                make_map()
        else:
            print "You can't walk through a wall!"
            action() 

def door():
    print "You found a door!"
def guards():
    print "You found three guards!"
def syrup():
    print "You found a bottle of syrup!"
def spoon():
    print "You found a spoon!"
def americans():
    print "You found your fellow Americans!"
def shrapnel():
    print "You found shrapnel!"
    
def items():
    decisions = {str(doorpos): door,
                str(guardpos): guards,
                str(syruppos): syrup,
                str(spoonpos): spoon,
                str(amerpos): americans,
                str(shrapnelpos): shrapnel}
    decisions[str(position)]()

    #decision = None
    # if (position==doorpos):
    #     door()
    # elif (position==guardpos):
    #     guards()
    # elif (position==syruppos):
    #     syrup()
    # elif (position==spoonpos):
    #     spoon()
    # elif (position==amerpos):
    #     americans()
    # elif (position==shrapnelpos):
    #     shrapnel()
    
def main():
    print "\n You have discovered the Slaughterhouse!"
    
    global space, door, position
    space[prow][pcolumn]=x
    make_map()
    
    while (found_door==False):
        action()
    
    
if __name__ == '__main__':
    main()