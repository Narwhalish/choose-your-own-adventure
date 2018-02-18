import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def move(pos):
    global zoo_grid
    global hp
    position = pos
    print 'Current HP: ' + str(hp) + '/300'
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    while True:
        command = raw_input('\n').strip().upper()
        if command == 'R':
            if position[0]<len(zoo_grid[0])-1:
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
            if position[1]<len(zoo_grid)-1:
                position[1]+=1
                break
            else: 
                print 'Cannot move down. Try again.'
        else:
            print 'Invalid input. Please try again.'
    hp-=5
    print position
    action(position)

def action(position):
    x, y = position[0], position[1]
    doStuff(x, y)
    move(position)

def doStuff(x, y):
    global backpack
    global hp
    global fridge
    if (x, y) == (0, 2):
        print 'You have found the refrigerator. Would you like to open it?\n'
        if yesorno():
            if fridge:
                print 'There is a continental breakfast in the fridge. How convenient!'
                displayImage('breakfast.jpg')
                print 'Would you like to take a bite of the continental breakfast?\n'
                if yesorno():
                    print 'You take a bite eagerly, only to find that cold muffins and danishes do not taste very good.'
                    print 'Loss of 10 HP points.'
                    print 'Disheartened, you put the breakfast back and continue.\n'
                    hp-=10
                else:
                    print 'Good for you! Cold breakfast would not taste very good.'
                    print 'However, a microwave would do a nice job of warming it up.'
                    print 'Add breakfast to backpack?'
                    if yesorno():
                        if len(backpack)<10:
                            backpack.append('breakfast')
                            fridge = False
                            print 'Added! Now time to find the microwave...\n'
                        else:
                            print 'No room in backpack. Item not added.\n'
                    else:
                        print 'Item not added.\n'
                return
            else:
                print 'The fridge is empty. Unfortunate.\n'
                return
        else:
            return
    if (x, y) == (1, 4):
        print 'You have found the microwave. Use it?\n'
        displayImage('microwave.jpg')
        if yesorno():
            if 'breakfast' in backpack:
                print 'You microwave your continental breakfast. Yum! Toasty muffins and danishes.'
                print 'Add 50 HP points.'
                hp+=50
            else:
                print 'You don\'t have anything to microwave.'
            return
        else:
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

global backpack
backpack = []
global jp
hp = 300
global zoo_grid
zoo_grid = [[0 for x in range(5)] for y in range(5)]
global fridge
fridge = True

start = [0, 0]


print 'You wake up, delirious and foggy-eyed.'
print 'It is strangely cold, and upon looking down, you realize that you are completely naked.'
print '\"Oh no,\" you think to yourself. \"Not again.\"'
print 'You are on the Planet Tralfamadore, on exhibit in a Tralfamadorian Zoo.\n'

move(start)