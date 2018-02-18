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
space[prow][pcolumn]=x
def print_space():
    for row in space:
        print row
        print '\n'
        # if row[2]==space[2][2]:
        #     space[2][2]=x
    
def action():
    global prow, pcolumn
    action = raw_input('Up, Down, Right, Left (U,D,R,L): ')
    if 'U':
        space[prow][pcolumn]=0
        space[prow-1][pcolumn]=x
        print_space()

def main():
    print_space()
    action()
    
if __name__ == '__main__':
    main()