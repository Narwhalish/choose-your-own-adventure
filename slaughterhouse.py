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
================================================================================
"""
import matplotlib.pyplot as plt

global space, position
space = [[0]*5 for i in range(5)]
global prow, pcolumn
prow = 2
pcolumn = 2
x = "You"

def print_space():
    global space
    for row in space:
        print row
        print '\n'

def make_map():
    global space
    print "global"
    print_space()
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
    global prow, pcolumn, space
    action = raw_input('Up, Down, Right, Left (U,D,R,L): ')
    if ( action == 'U'):
        space[prow][pcolumn]=0
        if prow!=0:
            prow=prow-1
            space[prow][pcolumn]=x
            make_map()
        else:
            print "You can't walk through a wall!"
            #action() 
    if (action=='D'):
        space[prow][pcolumn]=0
        if prow!=4:
            prow=prow+1
            space[prow][pcolumn]=x
            make_map()
        else:
            print "You can't walk through a wall!"
            #action() 

def main():
    global space
    space[prow][pcolumn]=x
    make_map()
    action()
    
if __name__ == '__main__':
    main()