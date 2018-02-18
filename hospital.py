import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def move(pos):
    global hospital_grid
    position = pos
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    while True:
        command = raw_input('\n').strip().upper()
        if command == 'R':
            if position[0]<len(hospital_grid[0])-1:
                position[0]+=1
                break
            else: 
                print 'Cannot move right. Try again.'
        elif command == 'L':
            if position[0]>0:
                position[0]-=1
                break
            else: 
                print 'Cannot move left. Try again.'
        elif command == 'U':
            if position[1]>0:
                position[1]-=1
                break
            else: 
                print 'Cannot move up. Try again.'
        elif command == 'D':
            if position[1]<len(hospital_grid)-1:
                position[1]+=1
                break
            else: 
                print 'Cannot move down. Try again.'
        else:
            print 'Invalid input. Please try again.'
    action(position)

def action(position):
    x, y = position[0], position[1]
    doStuff(x, y)
    move(position)

def doStuff(x, y):
    pass

def yesorno():
    while True:
        command = raw_input('Enter \'Y\' for yes or \'N\' for no: ')
        if command.strip().upper() == 'Y':
            return True
        elif command.strip().upper() == 'N':
            return False
        else:
            print 'Command not recognized. Try again.'
            
def displayImage(name):
    image = mpimg.imread(name)
    ax = plt.axes(frameon=False)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(image)
    plt.show()

def makeMap(pos):
    data = [row[:] for row in hospital_grid]
    data[pos[1]][pos[0]] = 'YOU ARE HERE'
    color_grid = [['black' for x in range(5)] for y in range(5)]
    color_grid[pos[1]][pos[0]] = 'indigo'
    table = plt.table( #initialize table
        cellText=data,
        cellColours=color_grid,
        cellLoc='center',
        colLoc='center',
        loc='center',bbox=None)
    table.scale(1, 3.65)
    plt.xticks([], [])
    plt.yticks([], [])
    table_props = table.properties()
    table_cells = table_props['child_artists']
    for cell in table_cells:
        cell._text.set_color('white')
        cell.set_edgecolor('white')
    plt.show()

global backpack
backpack = []
global hospital_grid
hospital_grid = [['' for x in range(5)] for y in range(5)]

start = [0, 0]

print '\n***\n'
#insert storyline

move(start)