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

global space
space = [[0]*5 for i in range(5)]
global prow, pcolumn
prow = 2
pcolumn = 2
x = 1
# for row in range(5):
#     for i in range(5):
#         print i
#         space[row][i]=x
#         x+=1

def print_space():
    for row in space:
        print row
        print '\n'

def make_map():
    data = [row[:] for row in space]
    color_grid = [['black']*5 for i in range(5)]
    pmap = plt.figure()
    plt.xticks([])
    plt.yticks([])
    tmap = plt.table(cellText=data, cellColours=color_grid,
            cellLoc='center', rowLoc='left', colLoc = 'center',
            loc='center', bbox=None)
    tmap.scale(1, 3.65)
    table_cells = tmap.properties()['child_artists']
    for cell in table_cells:
        cell._text.set_color('white')
        cell.set_edgecolor('white')
    plt.show()

def action():
    global prow, pcolumn
    action = raw_input('Up, Down, Right, Left (U,D,R,L): ')
    if 'U':
        space[prow][pcolumn]=0
        space[prow-1][pcolumn]=x
        make_map()

def main():
    space[prow][pcolumn]=x
    make_map()
    #print_space()
    action()
    
if __name__ == '__main__':
    main()