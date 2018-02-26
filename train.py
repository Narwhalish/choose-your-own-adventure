'''Choose Your Own Adventure: Train
Code for the train room. User must satisfy all basic needs (food, water, sleep) to be able to leave.
Leads from: Woods
Leads to: Hospital
Objects:
    Food x2
    Water x1
    Sleep x1
    Wild Bob
    Hobo
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import hospital
import backpack

def move(pos): #Accepts user input to move through room
    global train_grid
    global hp, bp
    position = pos #current position 
    print '-'*100
    if not endable: #whether or not user has all needs fulfilled
        checkVitals() #check to see if HP has been drained or score has been reached
        print 'Needs fulfilled: ' 
        print '\tFood: ' + str(food) + '/2'
        print '\tWater: ' + str(water) + '/1'
        print '\tSleep: ' + str(sleep) + '/1'
    #print instructions for user
    print 'Current HP: ' + str(hp) + '/150'
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    print 'Enter \'MAP\' to display a map of uncovered objects'
    print 'Enter \'BACKPACK\' to access backpack functions'
    
    #loops until user gives valid input
    while True:
        command = raw_input('\n').strip().upper()
        if command == 'R':
            if position[0]<len(train_grid[0])-1: #makes sure user is not at edge of room
                position[0]+=1 #move right
                break
            else: 
                print 'Cannot move right. Try again.'
        elif command == 'L':
            if position[0]>0: #makes sure user is not at edge of room
                position[0]-=1 #move left
                break
            else: 
                print 'Cannot move left. Try again.'
        elif command == 'U':
            if position[1]>0: #makes sure user is not at edge of room
                position[1]-=1 #move up
                break
            else: 
                print 'Cannot move up. Try again.'
        elif command == 'D':
            if position[1]<len(train_grid)-1: #makes sure user is not at edge of room
                position[1]+=1 #move down
                break
            else: 
                print 'Cannot move down. Try again.'
        elif command == 'MAP':
            hp-=25
            makeMap(position) #call function to display map
            move(position) #calls move function anew
        elif command == 'BACKPACK':
            bp, hp = backpack.main(bp, hp) #call function to print backpack contents
            move(position) #calls move function anew
        else:
            print 'Invalid input. Please try again.'
    hp-=5
    action(position) #call function to act based on new position

def action(position): #Acts based on new user position
    x, y = position[0], position[1]
    doStuff(x, y) #calls function to perform action
    move(position) #call move() for next user movement

def doStuff(x, y): #Runs interactive code based on user position
    global backpack
    global hp
    global food, water, sleep
    global bread, jerky, puddle
    
    if (x, y) == (2, 2):
        if not bread:
            print 'You find a hunk of bread!'
            displayImage('bread.JPG')
            print 'Consume bread?'
            if yesorno():
                if not endable:
                    food+=1
                    print 'The bread is stale, but you are so hungry that it tastes delicious!'
                    bread = True
                    train_grid[2][2] = 'Eaten!'
                else:
                    print 'You have already eaten enough!'
            else:
                train_grid[2][2] = 'Food' #add to map
        else: 
            print 'Nothing here!'
        return
        
    elif (x, y) == (3, 4):
        if not jerky:
            print 'You find a hunk of jerky!'
            displayImage('jerky.jpg')
            print 'Consume jerky?'
            if yesorno():
                if not endable:
                    food+=1
                    print 'Mmm...the salty jerky makes your taste buds sing.'
                    jerky = True
                    train_grid[4][3] = 'Eaten!'
                else:
                    print 'You have already eaten enough!'
            else:
                train_grid[0][0] = 'Food' #add to map
        else: 
            print 'Nothing here!'
        return
    
    elif (x, y) == (4, 2):
        if not puddle:
            print 'You find a puddle of water!'
            displayImage('puddle.jpg')
            print 'Drink water?'
            if yesorno():
                if not endable:
                    water+=1
                    print 'The water is brackish, but you are so thirsty that you don\'t notice.'
                    puddle = True
                    train_grid[2][4] = 'Drank!'
                else:
                    print 'You have already drank enough!'
            else:
                train_grid[0][0] = 'Water' #add to map
        else: 
            print 'Nothing here!'
        return            
    
    elif (x, y) == (1, 1):
        train_grid[1][1] = 'Wild Bob' #add to map
        print 'It\'s Wild Bob and he does not look very happy. Speak with him?\n'
        displayImage('weary.jpg')
        if yesorno(): #if speak to Wild Bob
            print '\"What are you doing in my private space?\" he shouts.'
            print 'He then proceeds to punch you in the gut.'
            print 'Loss of 100 HP'
            hp-=100
        else:
            print 'You ignore Wild Bob and continue on your quest.'
        return
        
    elif (x, y) == (1, 4):
        train_grid[4][1] = 'Hobo' #add to map
        print 'You spy a hobo in the corner, looking tired and defeated. Speak with him?\n'
        displayImage('weary.jpg')
        if yesorno(): #if speak to hobo
            print '\"Useless soldier! Leave me alone!\" he shouts.'
            print 'He then proceeds to kick you in the face.'
            print 'Loss of 100 HP'
            hp-=100
        else:
            print 'You ignore the hobo and continue on your quest.'
        return
        
    elif (x, y) == (4, 1):
        train_grid[1][4] = 'Sleep'
        print 'You found a small nook to sleep in!'
        print 'Sleep?'
        if yesorno():
            if sleep < 1:
                sleep+=1
                print 'Even in such a small space, you relish the short rest.'
            else:
                print 'Having already taken a rest, you cannot fall asleep again.'
        else:
            print 'You decide against sleeping and continue on your journey.'
        return   
    
    elif (x, y) == (2, 4):
        print 'You have found the exit!'
        if endable:
            print 'As you step out of the boxcar, you begin to feel a little woozy...'
            print 'Your clocks begin to turn as you become unstuck in time again.'
            hospital.main(bp, hp, eggs)
        else:
            print 'You\'re too drained to do anything else right now. Keep looking for those essentials!'
        
    else:
         print 'Nothing here!'
         return 

def yesorno(): #General function to ask user yes-or-no question
    #loop until user gives proper input
    while True:
        command = raw_input('Enter \'Y\' for yes or \'N\' for no: ')
        if command.strip().upper() == 'Y': #if yes
            return True
        elif command.strip().upper() == 'N': #if no
            return False
        else: #if improper input
            print 'Command not recognized. Try again.'
            
def displayImage(name): #General function to display image in kernel
    image = mpimg.imread(name)
    ax = plt.axes(frameon=False)
    #make axes invisible
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(image)
    plt.show() #show image

def checkVitals(): #Checks if HP and number of items are within bounds
    global hp
    if food==2 and water==1 and sleep ==1:
        endGame() #call function to end game
    if hp > 150: #hp exceeds bounds
        hp = 150
    if hp <=0: #hp deplenished 
        print 'Oh no! You have run out of HP!'
        print 'You will now be forced to sleep and restart.'
        print '\n...\n'
        reset() #call function to restart game
    return

def reset(): #Resets default values of global variables
    global hp
    hp = 150
    global food, water, sleep
    food, water, sleep = 0,0,0
    global bread, jerky, puddle
    bread, jerky, puddle = False, False, False
    global train_grid
    train_grid = [['' for x in range(5)] for y in range(5)]
    move([2,0]) #restart movement at bed square

def endGame(): #Function to continue narrative once user finds all items
    global endable
    endable = True #allows user to exit room
    
    print 'Congratulations! You have met all the necessities of survival.'
    askContinue()
    print '-'*100
    print 'Feeling newly energized, you decide to try to escape the boxcar.'
    print 'But how can you do that?'
    askContinue()
    print '\n***\n'
    print 'You have now been restored to your original position.'
    print 'To leave, search the boxcar to find the exit.'
    print 'As before, each step uses up valuable HP.'
    print 'If you run out, you will be forced to restart!'
    move([2,0])
    

def makeMap(pos): #Creates a map of user position and uncovered objects
    data = [row[:] for row in train_grid] #copy of zoo_grid
    data[pos[1]][pos[0]] = 'YOU ARE HERE' #maps user position
    color_grid = [['black' for x in range(5)] for y in range(5)]
    color_grid[pos[1]][pos[0]] = 'indigo'
    table = plt.table( #initialize table
        cellText=data,
        cellColours=color_grid,
        cellLoc='center',
        colLoc='center',
        loc='center',bbox=None)
    #format table
    table.scale(1, 3.65)
    plt.xticks([], [])
    plt.yticks([], [])
    table_props = table.properties()
    table_cells = table_props['child_artists']
    for cell in table_cells:
        cell._text.set_color('white')
        cell.set_edgecolor('white')
    plt.show() #display table

def askContinue(): #Delays display of text until user chooses to continue
    while True: #loops until user gives proper input
        command = raw_input('Enter \'C\' to continue: ')
        if command.strip().upper() == 'C': #if user continues
            return
        else:
            print 'Command not recognized. Try again.'

def main(b, h, e): #Function gives background narrative and calls move() for the first time
    #initialize global variables
    global bp
    bp = b
    global hp 
    hp = h
    global eggs 
    eggs = e
    global train_grid
    train_grid = [['' for x in range(5)] for y in range(5)]
    global endable
    endable = False
    global food, water, sleep
    food, water, sleep = 0, 0, 0
    global bread, jerky, puddle
    bread, jerky, puddle = False, False, False
    #start position
    start = [2, 0]
    
    #narrative
    print '\n***\n'
    print 'You find yourself packed into a boxcar with many other privates.'
    print 'World War I is still dragging on.'
    print 'Unfortunately, you have been captured by German soldiers.'
    askContinue() #delays display of text until user chooses to continue
    
    print '-'*100
    print 'There are narrow ventilators at the corners of the car.'
    print 'You stand under one of them, the crowd pressed against you.'
    askContinue()
    
    print '-'*100
    print 'From another boxcar, a man calls out through the ventilator that a man had just died.'
    print 'So it goes.'
    print 'You feel a sudden burst of fear. You want desperately to survive.'
    askContinue()
    
    print '-'*100
    print '\"Food. Water. Sleep,\" you think to yourself longingly.'
    print 'The conditions in the train car are terrible, but you must make do.'
    askContinue()

    print '\n***\n'
    
    print 'In order to survive, your must fulfill your basic necessities.'
    print 'Travel through the train car to find food, water, and sleep.'
    print 'Beware! Each step uses up valuable HP.'
    print 'If you run out of HP prematurely, you will be forced to restart.'
    
    print '\nAt any point, you may enter the command \'MAP\' to display a map of the room and the objects you have uncovered.'
    print 'However, doing so will invoke a cost of -25 HP.'
    print 'Choose wisely, and good luck!'
    askContinue() 
    
    print '\n***\n'
    
    move(start) #begin movement