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
global position
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

for row in space:
     print row
     print '\n'
     # if row[2]==space[2][2]:
     #     space[2][2]=x

def main():
    action()
    
def action():
    action = raw_input('Up, Down, Right, Left (U,D,R,L): ')
    if 'U':
        space[prow][pcolumn]=0
        prow=prow-1
        space[prow][pcolumn]=x
        
    
if __name__ == '___main___':
    main()