import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def move(pos):
    global hospital_grid
    global hp
    position = pos
    if not endable:
        checkVitals() #check to see if HP has been drained or score has been reached
        print 'Current books: ' 
        for book in books:
            print '\t' + book
        if len(books)==0:
            print '\tNone'
        print ''
    print 'Current HP: ' + str(hp) + '/150'
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    print 'Enter \'MAP\' to display a map of uncovered objects'
    
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
        elif command == 'MAP':
            makeMap(position) #call function to display map
            hp-=25
            move(position) #calls move function anew
        else:
            print 'Invalid input. Please try again.'
    action(position)

def action(position):
    x, y = position[0], position[1]
    doStuff(x, y)
    move(position)

def doStuff(x, y):
    global backpack
    global hp
    global books
    global drawer
    
    if (x, y) == (0, 0):
        hospital_grid[0][0] = 'Bed'
        print 'You have found your hospital bed.'
        displayImage('hospitalbed.jpg')
        while True:
            command = raw_input('To take a quick nap, enter \'1\'. To look under mattress, enter \'2\': ')
            if command.strip() == '1':
                print 'You hop in and snooze for a while.'
                print 'Add 50 HP points.\n'
                hp+=50
                break
            elif command.strip() == '2':
                if 'The Gospel from Outer Space' not in books:
                    print '\nTo your surprise, you find a dusty book under your mattress.'
                    print 'The title is "The Gospel from Outer Space" -- by Kilgore Trout.'
                    print 'It seems that you borrowed one of Rosewater\'s novels and forgot to return it. Whoops!\n' 
                    books.append('The Gospel from Outer Space')
                else:
                    print 'Nothing here!'
                break
            else:
                print 'Command not recognized. Try again.'
        return
        
    elif (x, y) == (2, 0):
        hospital_grid[0][2] = 'Rosewater'
        print 'You have found Eliot Rosewater\'s bed. Look under the mattress?\n'
        displayImage('rosewater.jpg')
        if yesorno():
            print 'Rosewater, having been in the middle of a nap, jolts awake as you lift his bed.'
            print '\"What are you doing?!\" he shrieks. He then proceeds to sock you in the face out of self defense.'
            print 'Loss of 50 HP points.\n'
            hp-=50
        return
    
    elif (x, y) == (0, 2):
        hospital_grid[2][0] = 'Drawer'
        print 'You have found your bedside drawer.'
        displayImage('table.jpg')
        while True:
            command = raw_input('Open Drawer 1 (\'1\'), Drawer 2 (\'2\'), Drawer 3 (\'3\'), or none (\'0\')? ')
            if command.strip() == '1':
                print 'Ouch! There is an ashtray with a cigarette still burning in the first drawer.'
                print 'You burn your finger and burst out into pitiful tears.'
                print 'Loss of 20 HP points.\n'
                hp-=20
                break
            elif command.strip() == '2':
                if drawer:
                    print 'You find a light blue pill in the second drawer. When used, it can restore 15 HP points. Add to backpack?\n'
                    if yesorno():
                        if len(backpack)<10: 
                            backpack.append('pill')
                            drawer = False
                            print 'Added!\n'
                        else:
                            print 'No room in backpack. Item not added.\n'
                    else:
                        print 'Item not added.\n'
                else:
                    print 'The drawer is empty!\n'
                break
            elif command.strip() == '3':
                print 'Aha! You find a Kilgore Trout book entitled \"The Big Board.\"'
                print 'It seems you are quite lousy at returning the books you borrow from Rosewater.\n'
                books.append('The Big Board')
                break
            elif command.strip() == '0':
                break
            else:
                print 'Command not recognized. Try again.'
        return
            
    elif (x, y) == (3, 1):
        hospital_grid[3][1] = 'Trunk'
        print 'You have found Rosewater\'s steamer trunk.'
        displayImage('trunk.jpg')
        print 'Open trunk?\n'
        if yesorno():
            if 'The Gutless Wonder' not in books:
                print 'You find \"The Gutless Wonder\" by Kilgore Trout.'
                print '\"Rosewater, you idiot!\" you exlaim. \"One of your books is right here!\"'
                print 'Eliot Rosewater throws a pillow at you. It hurts.\n'
                books.append('The Gutless Wonder')
            else:
                print 'Nothing here!\n'
        return
        
    else:
        print 'Nothing here.\n'
        return
                    

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

def checkVitals():
    global hp
    if len(books) == 5: 
        print 'Congratulations! You have found all five books.'
        print '\n***\n'
        endGame()
    if hp > 150: #hp exceeds bounds
        hp = 150
    if hp <=0: #hp deplenished 
        print 'Oh no! You have run out of HP!'
        print 'You will now be forced to sleep and restart.'
        print '\n...\n'
        reset() #call function to restart game
    return

def reset():
    global books
    books = []
    global hp
    hp = 150
    global hospital_grid
    hospital_grid = [['' for x in range(5)] for y in range(5)]

def endGame():
    pass

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

def askContinue(): #Delays display of text until user chooses to continue
    while True: #loops until user gives proper input
        command = raw_input('Enter \'C\' to continue: ')
        if command.strip().upper() == 'C': #if user continues
            return
        else:
            print 'Command not recognized. Try again.'

global backpack
backpack = []
global hp
hp = 150
global books 
books = []
global hospital_grid
hospital_grid = [['' for x in range(5)] for y in range(5)]
global endable
endable = False
global drawer, trunk
drawer = True

start = [0, 0]

def main():
    print '\n***\n'
    print 'You wake up to the acrid smell of sterile sheets and antiseptic.'
    print 'The sun is obscenely bright shining in from the open window, and your shield your eyes as you look around.'
    askContinue()
    
    print 'You are lying in bed at a veterans hospital near Lake Placid, New York.'
    print 'It is still early morning. In the bed to your left lies Eliot Rosewater, a former infantry captain and avid Kilgore Trout fan.'
    print 'He sits propped up against his pillows, staring forlorningly at the whitewashed wall.'
    askContinue()
    
    print '\"Rosewater!\" you exclaim. \"Have they been playing with your clocks too?\"'
    askContinue()
    
    print '\"My clocks? No. My clocks are fine. They\'ve been playing with my books, though.\"'
    print 'He frowns, looking down sadly at his folded hands.'
    print '\"All of my Kilgore Trout books-- gone! I can\'t find them anywhere.\"'
    askContinue()
    
    print '\"That\'s a pity, Rosewater.\"'
    print 'You pause for a moment to think. \"Say, if I help you find your books, will you help me find the person playing with my clocks?\"'
    askContinue()
    
    print '\"I have no idea what that means, but I do want my books back. Sure, why not?\"'
    askContinue()
    
    print '\n***\n'
    
    print 'In order to enlist Eliot Rosewater\'s help, you must find his missing Kilgore Trout books.'
    print 'There are a total of five of them scattered throughout your hospital room.'
    print 'Interact with objects and people in order to find them.' 
    print 'Beware of dangerous items, however. They may damage your HP.'
    print 'If you run out of HP, you will be forced to sleep and restart this chapter of the game.\n'
    
    print 'At any point, you may enter the command \'MAP\' to display a map of the room and the objects you have uncovered.'
    print 'However, doing so will invoke a cost of -25 HP.'
    print 'Choose wisely, and good luck!'
    askContinue() 
    
    print '\n***\n'
    
    move(start)