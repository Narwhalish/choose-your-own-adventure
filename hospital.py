'''Choose Your Own Adventure: Hospital
Code for the hospital room. User must find five Kilgore Trout books in the room 
to be able to exit. Must achieve score before running out of HP. 
Leads from: Train
Leads to: Office
Objects:
    Hospital bed
    Rosewater
    Steamer trunk
    Drawer
    Valencia
    Nurse
    Loose Floorboard
    Art collage
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import backpack
import office

def move(pos): #Accepts user input to move through room
    global hospital_grid
    global hp
    global bp
    position = pos #current position 
    print '-'*100
    if not endable: #if user has not yet found all five books
        checkVitals() #check to see if HP has been drained or score has been reached
        print 'Current books: ' 
        for book in books: #print list of found books
            print '\t' + book
        if len(books)==0: #if no books found
            print '\tNone'
        print ''
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
            if position[0]<len(hospital_grid[0])-1: #makes sure user is not at edge of room
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
            if position[1]<len(hospital_grid)-1: #makes sure user is not at edge of room
                position[1]+=1 #move down
                break
            else: 
                print 'Cannot move down. Try again.'
        elif command == 'MAP':
            makeMap(position) #call function to display map
            hp-=25
            move(position) #calls move function anew
        elif command == 'BACKPACK':
            bp, hp = backpack.main(bp, hp) #call function to print backpack contents
            move(position) #calls move function anew
        else:
            print 'Invalid input. Please try again.'
    action(position) #call function to act based on new position

def action(position): #Acts based on new user position
    x, y = position[0], position[1]
    doStuff(x, y) #calls function to perform action
    move(position) #call move() for next user movement

def doStuff(x, y): #Runs interactive code based on user position
    global bp
    global hp
    global books
    global drawer
    
    if (x, y) == (0, 0):
        hospital_grid[0][0] = 'Bed' #add to map
        print 'You have found your hospital bed.'
        displayImage('hospitalbed.jpg')
        while True: #loop until user gives proper input
            command = raw_input('To take a quick nap, enter \'1\'. To look under mattress, enter \'2\': ')
            if command.strip() == '1': #if nap
                print 'You hop in and snooze for a while.'
                print 'Add 50 HP points.\n'
                hp+=50
                break
            elif command.strip() == '2': #if look under mattress
                if 'The Gospel from Outer Space' not in books:
                    print '\nTo your surprise, you find a dusty book under your mattress.'
                    print 'The title is "The Gospel from Outer Space" -- by Kilgore Trout.'
                    print 'It seems that you borrowed one of Rosewater\'s novels and forgot to return it. Whoops!\n' 
                    books.append('The Gospel from Outer Space') #add novel to list of found books
                else:
                    print 'Nothing here!'
                break
            else:
                print 'Command not recognized. Try again.'
        return
        
    elif (x, y) == (2, 0):
        hospital_grid[0][2] = 'Rosewater' #add to map
        print 'You have found Eliot Rosewater\'s bed. Look under the mattress?\n'
        displayImage('rosewater.jpg')
        if yesorno(): #if look under mattress
            print 'Rosewater, having been in the middle of a nap, jolts awake as you lift his bed.'
            print '\"What are you doing?!\" he shrieks. He then proceeds to sock you in the face out of self defense.'
            print 'Loss of 50 HP points.\n'
            hp-=50
        return
    
    elif (x, y) == (1, 2):
        hospital_grid[2][1] = 'Drawer' #add to map
        print 'You have found your bedside drawer.'
        displayImage('table.jpg')
        while True: #loop until user gives proper input
            command = raw_input('Open Drawer 1 (\'1\'), Drawer 2 (\'2\'), Drawer 3 (\'3\'), or none (\'0\')? ')
            if command.strip() == '1': #Drawer 1
                print 'Ouch! There is an ashtray with a cigarette still burning in the first drawer.'
                print 'You burn your finger and burst out into pitiful tears.'
                print 'Loss of 20 HP points.\n'
                hp-=20
                break
            elif command.strip() == '2': #Drawer 2
                if drawer: #if drawer has not been opened yet
                    print 'You find a light blue pill in the second drawer. When used, it can restore 15 HP points. Add to backpack?\n'
                    if yesorno():
                        if len(bp)<5: #add to backpack if sufficient room 
                            bp.append('pill')
                            drawer = False
                            print 'Added!\n'
                        else:
                            print 'No room in backpack. Item not added.\n'
                    else:
                        print 'Item not added.\n'
                else: #if drawer has already been opened
                    print 'The drawer is empty!\n'
                break
            elif command.strip() == '3': #Drawer 3
                if 'The Big Board' not in books: #if book has not been taken yet
                    print 'Aha! You find a Kilgore Trout book entitled \"The Big Board.\"'
                    print 'It seems you are quite lousy at returning the books you borrow from Rosewater.\n'
                    books.append('The Big Board') #add novel to list of found books
                else: #if book has already been taken
                    print 'The drawer is empty!'
                break
            elif command.strip() == '0':
                break
            else:
                print 'Command not recognized. Try again.'
        return
            
    elif (x, y) == (3, 1):
        hospital_grid[1][3] = 'Trunk' #add to map
        print 'You have found Rosewater\'s steamer trunk.'
        displayImage('trunk.jpg')
        print 'Open trunk?\n'
        if yesorno():
            if 'The Gutless Wonder' not in books: #if book had not been taken yet
                print 'You find \"The Gutless Wonder\" by Kilgore Trout.'
                print '\"Rosewater, you idiot!\" you exlaim. \"One of your books is right here!\"'
                print 'Eliot Rosewater throws a pillow at you. It hurts.\n'
                books.append('The Gutless Wonder') #add novel to list of found books
            else: #if book has already been taken
                print 'Nothing here!\n'
        return
    
    elif (x, y) == (3, 3):
        hospital_grid[3][3] = 'Nurse' #add to map
        print 'You have found a nurse in your room.'
        displayImage('nurse.jpg')
        print 'Speak to her?'
        if yesorno():
            if 'hospitaladithya' not in eggs: #if adithya has not been taken yet
                print '\"Hi!\" she says in greeting. \"I have a question for you-- what is the best snack?\"'
                while True: #loop until user gives proper input
                    print '\nFor \'pretzels,\' enter 0.'
                    print 'For \'chocolate,\' enter 1.'
                    print 'For \'Goldfish,\' enter 2.'
                    print 'For \'granola bar,\' enter 3.'
                    command = raw_input('What would you like to choose? ')
                    if command.strip() == '2': #if correct answer 
                        print '\nThe nurse grins wildly, clapping her hands in delight.'
                        print '\"Awesome!\" she exclaims. \"That\'s exactly what I thought. Here, take this as a token of my gratitude.\"'
                        print 'She hands you a small figurine of a very comely young man.'
                        displayImage('adithya2.png')
                        print 'You are not sure of its purpose, but you accept the gift nonetheless and continue on your search.\n'
                        eggs.append('hospitaladithya') #add figurine to list of found adithyas
                        break
                    elif command.strip() in ('0','2','3'): #if incorrect answer 
                        print '\nThe nurse frowns in disappointment.'
                        print '\"Dangit,\" she says. \"I don\'t seem to agree.. oh well. Carry on.\"'
                        print 'Confused, you turn away and continue on your search.\n' 
                        break
                    else: 
                        print 'Command not recognized. Try again.'
            else:
                print 'The nurse recognizes you and smiles.'
                print '\"Hello! It was very pleasant speaking to you before. I am quite busy now, though. No time for chit chat!\"'
                print 'You leave her to her work and continue on your search.\n'
        else:
            print 'You ignore the nurse and continue on your search.\n'
        return
    
    elif (x, y) == (1, 4):
        hospital_grid[4][1] = 'Floorboard' #add to map
        print 'You have a loose floorboard.'
        displayImage('floor.jpeg')
        print 'Lift floorboard?\n'
        if yesorno():
            if 'Maniacs in the Fourth Dimension' not in books: #if book has not been taken yet
                print 'After clearing away the dust, you find \"Maniacs in the Fourth Dimesnion\" by Kilgore Trout.'
                print 'Somehow, it has ended up hidden underneath the floor. How strange... \n'
                books.append('Maniacs in the Fourth Dimension') #add novel to list of found books
            else: #if book has already been taken
                print 'Nothing here!\n'
        return
    
    elif (x, y) == (4, 2):
        hospital_grid[2][4] = 'Valencia' #add to map
        print 'You find your wife, Valencia, sitting at the side of the room.'
        print 'She is fast asleep, a half-eaten Three Musketeers candy bar still in her hand.'
        displayImage('valencia.jpg')
        print 'Interact?'
        if yesorno():
            while True: #loop until user gives proper input
                command = raw_input('Wake up (\'1\'), look in purse (\'2\'), or take candy bar (\'3\')? ')
                if command.strip() == '1': #wake up
                    print 'You shake Valencia\'s shoulder gently. She jolts awake with a shriek.'
                    print '\"FIND ME AMONGST THE GHOSTS!!\" she exclaims, whacking you in the face in the process.'
                    print 'You cradle your swollen eye in pain as Valencia promptly falls back asleep.'
                    print 'Loss of 20 HP points.\n'
                    hp-=20
                    break
                elif command.strip() == '2': #look in purse
                    print 'Channeling your inner ninja skills, you sneak a glance into Valencia\'s purse.'
                    if 'The Money Tree' not in books: #if book has not been taken yet
                        print 'Sure enough, there\'s a Kilgore Trout book in it entitled \"The Money Tree.\"'
                        print 'Unfortunately, the book is covered in chocolate stains. You hope Rosewater doesn\'t mind...\n'
                        books.append('The Money Tree') #add novel to list of found books
                    else: #if book has already been taken
                        print 'Unfortunately, there\'s nothing in it.'
                    break
                elif command.strip() == '3': #take candy bar
                    print 'Your stomach growling, you gingerly remove the candy bar from Valencia\'s grasp.'
                    print 'She snores as if in protest, but doesn\'t wake up.'
                    print 'You take a bite. Mmm... stale, but still delicious!'
                    print 'Add 20 HP points.'
                    hp+=20
                    break
                else:
                    print 'Command not recognized. Try again.'
        else:
            print 'You ignore Valencia and continue on your search.\n'
        return
        
    elif (x, y) == (4, 4):
        hospital_grid[4][4] = 'Photo' #add to map
        print 'You find a framed photo collage of two lovely figure skaters on the wall.'
        displayImage('shomayuzu.jpg')
        if not endable: #if user has not found all five books yet
            print 'How adorable!\n'
        else: #if user has found all five books
            print 'Perhaps this is the piece of artwork Rosewater mentioned.'
            print 'It certainly is quite aesthetically pleasing.'
            askContinue()
            print 'As you gaze at the collage, a surge of affectionate emotion overcomes you.'
            print 'Your breath quickens... your heart flutters... and you feel yourself becoming unstuck in time again...'
            office.main(bp, hp, eggs) #exit room
        return
        
    else:
        print 'Nothing here!\n'
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

def checkVitals(): #Checks if HP and number of books are within bounds
    global hp
    if len(books) == 5: #user has found all five books
        print 'Congratulations! You have found all five books.'
        print '\n***\n'
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
    global books
    books = []
    global hp
    hp = 150
    global hospital_grid
    hospital_grid = [['' for x in range(5)] for y in range(5)]
    move([0,0]) #restart movement at bed square

def endGame(): #Function to continue narrative once user finds all books
    global endable
    endable = True #allows user to exit room
    
    print '\"Rosewater!\" you exclaim excitedly. \"I found all of your books!\"'
    print 'You hand the stack of novels to him, grinning from ear to ear.'
    askContinue()
    print '-'*100
    print '\"Thank you Billy Pilgrim,\" Rosewater says. \"I don\'t know what I\'d do without you.\"'
    print 'He flips open \"The Money Tree\" and begins to read.'
    askContinue()
    print '-'*100
    print '\"Um... didn\'t you say you were going to help me now?\" you ask, confused.'
    askContinue()
    print '-'*100
    print 'He blinks. \"Did I? How unfortunate. I have no idea how to help you.\"'
    askContinue()
    print '-'*100
    print 'You groan and collapse into a fetal position. \"I need to find out who\'s playing with my clocks!\"'
    askContinue()
    print '-'*100
    print 'Rosewater pauses in thought. \"Well, whenever I\'m feeling down, I like to look at artwork.\"'
    print 'He gestures vaguely at the other end of the room. \"One of my favorite pieces is over there. Maybe you should take a look.\"'
    askContinue()
    print '-'*100
    print 'Without any other leads, you decide to take Rosewater\'s advice.'
    print 'You must locate a piece of art in the hospital room in order to find your way out.'
    print 'As before, if you run out of HP, you will be forced to restart this chapter.'
    print 'Good luck!' 
    askContinue()
    print '\n***\n'
    
    move([2,0]) #restart movement starting at Rosweater's bed

def makeMap(pos): #Creates a map of user position and uncovered objects
    data = [row[:] for row in hospital_grid] #copy of zoo_grid
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
    global books 
    books = []
    global hospital_grid
    hospital_grid = [['' for x in range(5)] for y in range(5)]
    global endable
    endable = False
    global drawer
    drawer = True
    #start position
    start = [0, 0]
    
    #narrative
    print '\n***\n'
    print 'You wake up to the acrid smell of sterile sheets and antiseptic.'
    print 'The sun is obscenely bright shining in from the open window, and your shield your eyes as you look around.'
    askContinue() #delays display of text until user chooses to continue
    
    print '-'*100
    print 'It is 1948, three years after the end of the war.'
    print 'You are lying in bed at a veterans hospital near Lake Placid, New York.'
    print 'It is still early morning. In the bed to your left lies Eliot Rosewater, a former infantry captain and avid Kilgore Trout fan.'
    print 'He sits propped up against his pillows, staring forlorningly at the whitewashed wall.'
    askContinue()
    
    print '-'*100
    print '\"Rosewater!\" you exclaim. \"Have they been playing with your clocks too?\"'
    askContinue()
    
    print '-'*100
    print '\"My clocks? No. My clocks are fine. They\'ve been playing with my books, though.\"'
    print 'He frowns, looking down sadly at his folded hands.'
    print '\"All of my Kilgore Trout books-- gone! I can\'t find them anywhere.\"'
    askContinue()
    
    print '-'*100
    print '\"That\'s a pity, Rosewater.\"'
    print 'You pause for a moment to think. \"Say, if I help you find your books, will you help me find the person playing with my clocks?\"'
    askContinue()
    
    print '-'*100
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
    
    move(start) #begin movement