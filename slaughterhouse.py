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

x = 1
# for row in range(5):
#     for i in range(5):
#         print i
#         space[row][i]=x
#         x+=1
space[2][2]=x

for row in space:
     print row
     print '\n'
     # if row[2]==space[2][2]:
     #     space[2][2]=x

def main():
    action()
    
def action():
    action = raw_input('Up, Down, Right, Left (U,D,R,L): ')
    #if U:
        
    
if __name__ == '___main___':
    main()