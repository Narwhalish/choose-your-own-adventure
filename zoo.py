'''Choose Your Own Adventure: Zoo
Code for the zoo room. Implements an HP and score system to determine when gameplay is over.
 
Objects:
    Bathroom
    Bed
    Montana Wildhack
    Television
    Refrigerator
    Microwave
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def move(pos): #Accepts user input to move through room
    global zoo_grid
    global hp
    global score
    position = pos #current position 
    
    #print instructions for user
    print 'Current HP: ' + str(hp) + '/150'
    print 'Current score: ' + str(score) + '/50'
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    print 'Enter \'MAP\' to display a map of uncovered objects'
    
    #loops until user gives valid input
    while True:
        command = raw_input('\n').strip().upper()
        if command == 'R': 
            if position[0]<len(zoo_grid[0])-1: #makes sure user is not at edge of room
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
            if position[1]<len(zoo_grid)-1: #makes sure user is not at edge of room
                position[1]+=1 #move down
                break
            else: 
                print 'Cannot move down. Try again.'
        elif command == 'MAP': 
            makeMap(position) #call function to display map
            hp-=25
            move(position) #calls move function anew
        else:
            print 'Invalid input. Please try again.'
    hp-=5
    action(position) #call function to act based on new position

def action(position): #Acts based on new user position
    x, y = position[0], position[1] 
    doStuff(x, y) #calls function to perform action
    checkVitals() #check to see if HP has been drained or score has been reached
    move(position) #call move() for next user movement

def doStuff(x, y): #Runs interactive code based on user position
    global backpack
    global hp
    global score
    global fridge
    global leaked
    global brushed
    global embraced
    global story
    
    #check if user's position is occupied by an interactive obkect
    if (x, y) == (0, 2):
        zoo_grid[2][0]='Fridge' #add to map
        print 'You have found the refrigerator. Would you like to open it?\n'
        
        if yesorno(): #asks yes-or-no question
            if fridge: #if fridge is unopened, prompt user action
                print 'There is a continental breakfast in the fridge. How convenient!'
                displayImage('breakfast.jpg') #print image to kernel
                print 'Would you like to take a bite of the continental breakfast?\n'
                if yesorno():
                    print 'You take a bite eagerly, only to find that cold muffins and danishes do not taste very good.'
                    print 'Loss of 10 HP points.'
                    print 'The Tralfamadorians, though, are somewhat amused by your disgust.'
                    print 'Add 5 audience satisfaction points.'
                    print 'Disheartened, you toss the breakfast into the trash and continue.\n'
                    
                    #update hp, score, global state of fridge
                    hp-=10
                    score+=5
                    fridge = False
                else:
                    print 'Good for you! Cold breakfast would not taste very good.'
                    print 'However, a microwave would do a nice job of warming it up.'
                    print 'Add breakfast to backpack?'
                    if yesorno():
                        if len(backpack)<10: #if there's room, add breakfast to bag
                            backpack.append('breakfast')
                            fridge = False
                            print 'Added! Now time to find the microwave...\n'
                        else:
                            print 'No room in backpack. Item not added.\n'
                    else:
                        print 'Item not added.\n'

            else: #if user has opened fridge before, print message
                print 'The fridge is empty. Unfortunate.\n'
        return
        
    elif (x, y) == (1, 4):
        zoo_grid[4][1]='Microwave'
        print 'You have found the microwave. Use it?\n'
        displayImage('microwave.jpg') #print image to kernel
        
        if yesorno():
            if 'breakfast' in backpack: #if user carries breakfast, allow them to use microwave
                print 'You microwave your continental breakfast. Yum! Toasty muffins and danishes.'
                print 'Add 50 HP points.'
                print 'The Tralfamadorians are fascinated by this strange device and its magical warming powers.'
                print 'Add 10 audience satisfaction points.'
                #update hp, score, global state of backpack
                hp+=50
                score+=10
                backpack.remove('breakfast')
            else: #if user doesn't have breakfast, print message
                print 'You don\'t have anything to microwave.'
        return
        
    elif (x, y) == (4, 0):
        zoo_grid[0][4]='Bed'
        print 'You have found the bed. Take a quick nap?\n'
        displayImage('bed.JPG') #print image to kernel
        
        if yesorno(): #asks yes-or-no question
            print 'You hop in and snooze for a while.'
            print 'Add 50 HP points.'
            print 'The Tralfamadorians, however, are bored by your state of torpor.'
            print 'Loss of 15 audience satisfaction points.\n'
            #update hp, score
            hp+=50
            score-=15
        return
        
    elif (x, y) == (2, 0):
        zoo_grid[0][2]='Bathroom'
        print 'You have found the bathroom. Enter?\n'
        displayImage('bathroom.jpg') #print image to kernel
        
        if yesorno():
            print 'Delightful! The room is a pleasant mint green, furnished with appliances from the Sears Roebuck warehouse in Iowa City, Iowa.'
            #loop until user gives proper input
            while True:
                command = raw_input('To brush teeth, enter \'1\'. To take a leak, enter \'2\': ')
                if command.strip() == '1': #to brush teeth
                    if brushed: #if user has already brushed
                        print 'The Tralfamadorian crowd, having already seen this performance, is underwhelmed.'
                        print 'Add 5 measly audience satisfaction points.\n'
                        score+=5
                    else: #if user has not brushed yet
                        print 'The Tralfamadorians are intrigued by the strange, bristly stick with which you rub your teeth.'
                        print 'Add 15 audience satisfaction points.\n'
                        score+=15
                        brushed = True
                    break
                elif command.strip() == '2': #to take a leak
                    if leaked: #if user has already taken a leak
                        print 'The Tralfamadorian crowd, having already seen this performance, is underwhelmed.'
                        print 'Add 5 measly audience satisfaction points.\n'
                        score+=5
                    else: #if user has not taken a leak yet
                        print 'The Tralfamadorian crowd goes wild at your display!'
                        print 'Add 25 audience satisfaction points.\n'
                        score+=25
                        leaked = True
                    break
                else:
                    print 'Command not recognized. Try again.'
        return 
        
    elif (x, y) == (3, 1):
        zoo_grid[1][3]='Montana'
        print 'You have found your amorous female companion, Montana Wildhack.'
        displayImage('montana.jpg') #print image to kernel
        print 'Interact?\n'
        
        if yesorno():
            #loop until user gives proper input
            while True: 
                print 'As you tap her on the shoulder, Montana turns around and smiles at you.'
                print '\"Tell me a story,\" Montana says.'
                print 'You have a wonderful story in mind, but you also happen to be feeling rather saucy.'
                command = raw_input('To embrace lovingly, enter \'1\'. To tell a story, enter \'2\': ')
                if command.strip() == '1': #to embrace lovingly
                    print '\nIgnoring Montana\'s request, you sweep her into your arms with grand romantic flourish.'
                    if embraced: #if user has already embraced
                        print 'Montana, now fed up that you have ignored her twice, pulls away and slaps you.'
                        print 'Loss of 15 HP.'
                        print 'The Tralfamadorians find the crude display of violence extremely unpleasant.'
                        print 'Loss of 10 audience satisfaction points.\n'
                        hp-=15
                        score-=10
                    else: #if user has not embraced yet
                        print 'The Tralfamadorian crowd is delighted, and so is Montana.'
                        print 'Add 15 audience satisfaction points.\n'
                        score+=15
                        embraced = True
                    break
                elif command.strip() == '2': #to tell a story
                    print '\nYou tell Montana about the bombing of Dresden and how the four guards, in their astonishment and grief, resembled a barber-shop quartet.'
                    if story: #if user has already told story
                        print 'The Tralfamadorians are quickly bored by the sound of human speech.'
                        print 'Loss of 5 audience satisfaction points.\n'
                        score-=5
                    else: #if story has not told story yet
                        print 'The Tralfamadorians find the story underwhelming and \"very human\".'
                        print 'However, they do enjoy hearing the strange noises of human speech.'
                        print 'Add 10 audience satisfaction points.\n'
                        score+=15
                        story = True
                    break
                else:
                    print 'Command not recognized. Try again.'
        return
        
    elif (x, y) == (3, 3):
        zoo_grid[3][3]='Television'
        print 'You have found the television, currently frozen on a western action film. Press play?\n'
        displayImage('television.jpg') #print image to kernel
        
        if yesorno():
            print 'You press the play button. Nothing happens.'
            print 'Press it again?\n'
            if yesorno(): #if user presses button twice
                print '\nConfused, you press the button again. Still nothing.'
                print 'You proceed to slam your fists at the screen and holler until you realize that the TV is nonfunctional.'
                print 'The image of one cowboy killing another is merely pasted to the screen!'
                print 'Mentally and physically drained, you proceed to cry for several hours.'
                print 'Loss of 25 HP.'
                print 'The Tralfamadorians, though, find your stupidity to be quite entertaining.'
                print 'Add 15 audience satisfaction points.\n'
                hp-=25
                score+=15
            else: #if user presses button only once
                print '\nYou intelligently deduce that the TV is nonfunctional.'
                print 'The image of one cowboy killing another is merely pasted to the screen!'
                print 'Filled with pride for your overwhelming logical reasoning skills, your mood is much improved.'
                print 'Add 15 HP points.\n'
                hp+=15
        return
        
    else: #if user's position is unoccupied
        print 'Nothing here.'
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
    plt.show() #show images

def checkVitals(): #Checks if HP and score values are within bounds
    global score
    global hp
    
    if score < 0: #negative score
        score = 0
    if score >= 50: #score met
        print 'Congratulations! You have successfully satisfied your audience.'
        print 'Your total score is: ' + str(score)
        print '\n***\n'
        raise SystemExit #end code
    if hp > 150: #hp exceeds bounds
        hp = 150
    if hp <=0: #hp deplenished
        print 'Oh no! You have run out of HP!'
        print 'You will now be forced to sleep and rejuvenate.'
        print '\n...\n'
        #reset hp and score values
        hp = 150
        score = 0
        move([4, 0]) #user restarts at bed square
    return

def makeMap(pos): #Creates a map of user position and uncovered objects
    data = [row[:] for row in zoo_grid] #copy of zoo_grid
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

#initialize global variables
global backpack
backpack = []
global hp
hp = 150
global score
score = 0
global zoo_grid
zoo_grid = [['' for x in range(5)] for y in range(5)]
global fridge
global leaked 
global brushed
global embraced
global story
fridge, leaked, brushed, embraced, story = True, False, False, False, False

#start position
start = [0, 0]

#narrative
print '\n***\n'
print 'You wake up, delirious and foggy-eyed.'
print 'It is strangely cold, and upon looking down, you realize that you are completely naked.'
print '\"Oh no,\" you think to yourself. \"Not again.\"'
print 'You are on the Planet Tralfamadore, on exhibit in a Tralfamadorian Zoo.\n'
print 'In order to return to Earth, you must entertain the Tralfamadorians!'
print 'Travel around the room and interact with objects in an effort to elevate your audience satisfaction score.'
print 'Don\'t dilly dally too much, though. Each step you take uses up valuable HP.'
print 'If you run out of HP, you will be forced to sleep and restart.\n'
print 'At any point, you may enter the command \'MAP\' to display a map of the zoo and the objects you have uncovered.'
print 'However, doing so will invoke a cost of -25 HP.'
print 'Choose wisely, and good luck!\n'

move(start) #begin movement