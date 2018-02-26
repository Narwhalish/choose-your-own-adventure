'''Choose Your Own Adventure: Woods
Code for the woods room. User must find all of Weary's belongings before they can be captured by the Germans. Objects must be found in particular order.
Leads to: Train
Objects:
    Bulletproof Bible
    Weary
    Trench Knife
    Gas Mask
    Bear Trap
    German Patrols
    Voodoo Doll
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def move(pos): #Accepts user input to move through room
    global woods_grid
    global hp
    position = pos #current position 
    print '-'*100
    if not endable: #whether or not user has found all of Weary's items
        checkInventory() #check to see if HP has been drained or score has been reached
        print 'Current items: ' 
        for item in items: #print list of found objects
            print '\t' + book
        if len(items)==0: #if no items found
            print '\tNone'
        print ''
    #print instructions for user
    print 'Current HP: ' + str(hp) + '/150'
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    print 'Enter \'MAP\' to display a map of uncovered objects'
    print 'Enter \'BACKPACK\' to print the current contents of your backpack'
    
    #loops until user gives valid input
    while True:
        command = raw_input('\n').strip().upper()
        if command == 'R':
            if position[0]<len(woods_grid[0])-1: #makes sure user is not at edge of room
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
            if position[1]<len(woods_grid)-1: #makes sure user is not at edge of room
                position[1]+=1 #move down
                break
            else: 
                print 'Cannot move down. Try again.'
        elif command == 'MAP':
            makeMap(position) #call function to display map
            move(position) #calls move function anew
        elif command == 'BACKPACK':
            print_backpack(backpack) #call function to print backpack contents
            move(position) #calls move function anew
        else:
            print 'Invalid input. Please try again.'
    action(position) #call function to act based on new position

def action(position): #Acts based on new user position
    x, y = position[0], position[1]
    doStuff(x, y) #calls function to perform action
    move(position) #call move() for next user movement

def doStuff(x, y): #Runs interactive code based on user position
    global backpack
    global hp
    global items
    
    if (x, y) == (0, 0):
        woods_grid[0][0] = 'Gas Mask' #add to map
        print 'You spot oddly shaped gas mask tangled on a mass of branches.'
        displayImage('gas_mask.jpg')
        while True: #loop until user gives proper input
            command = raw_input('To inspect it, enter \'1\'. To tug on it, enter \'2\'. To do nothing, enter \'0\': ')
            if command.strip() == '1': #if inspect
                print 'Yep, it\s really tangled up in there.'
                break
            elif command.strip() == '2' and 'Trench Knife' in items: #if has trench knife and cuts through straps
                if 'Gas Mask' not in items:
                    print '\nYou glance at the heavy trench knife in your hand.'
                    print 'In a glorious bout of ingenuity, you slice through the straps of the gas mask, freeing it from its wooden prison.'
                    print 'The glass lens are all scratched up. You can\'t see anything through them now! Oh well...'
                    items.append('Gas Mask') #add gas mask to list of found items
                else:
                    print 'Just a bunch of cut up fabric and branches.'
                break
            elif command.strip() == '0':
                break
            else:
                print 'Command not recognized. Try again.'
        return
        
    elif (x, y) == (1, 1):
        woods_grid[1][1] = 'Weary' #add to map
        print 'It\'s Weary and he does not look very happy. Speak with him?\n'
        displayImage('weary.jpg')
        if yesorno(): #if speak to Weary
            print '\"Have you found my stuff yet?\"'
            print '\"We don\'t have all day, you know.\"'
        return
    
    elif (x, y) == (3, 0):
        woods_grid[0][3] = 'Trench Knife' #add to map
        print 'You catch the glint of a shiny, serrated metal edge poking out from beneath a pile of leaves.'
        displayImage('table.jpg')
        
        return
            
    elif (x, y) == (3, 1):
        woods_grid[1][3] = 'Trunk' #add to map
        print 'You have found Rosewater\'s steamer trunk.'
        displayImage('trunk.jpg')
        print 'Open trunk?\n'
        if yesorno():
            if 'The Gutless Wonder' not in items: #if book had not been taken yet
                print 'You find \"The Gutless Wonder\" by Kilgore Trout.'
                print '\"Rosewater, you idiot!\" you exlaim. \"One of your items is right here!\"'
                print 'Eliot Rosewater throws a pillow at you. It hurts.\n'
                items.append('The Gutless Wonder') #add novel to list of found items
            else: #if book has already been taken
                print 'Nothing here!\n'
        return
    
    elif (x, y) == (3, 3):
        woods_grid[3][3] = 'Nurse' #add to map
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
        woods_grid[4][1] = 'Floorboard' #add to map
        print 'You have a loose floorboard.'
        displayImage('floor.jpeg')
        print 'Lift floorboard?\n'
        if yesorno():
            if 'Maniacs in the Fourth Dimension' not in items: #if book has not been taken yet
                print 'After clearing away the dust, you find \"Maniacs in the Fourth Dimesnion\" by Kilgore Trout.'
                print 'Somehow, it has ended up hidden underneath the floor. How strange... \n'
                items.append('Maniacs in the Fourth Dimension') #add novel to list of found items
            else: #if book has already been taken
                print 'Nothing here!\n'
        return
    
    elif (x, y) == (4, 2):
        woods_grid[2][4] = 'Valencia' #add to map
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
                    if 'The Money Tree' not in items: #if book has not been taken yet
                        print 'Sure enough, there\'s a Kilgore Trout book in it entitled \"The Money Tree.\"'
                        print 'Unfortunately, the book is covered in chocolate stains. You hope Rosewater doesn\'t mind...\n'
                        items.append('The Money Tree') #add novel to list of found items
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
        woods_grid[4][4] = 'Photo' #add to map
        print 'You find a framed photo collage of two lovely figure skaters on the wall.'
        displayImage('shomayuzu.jpg')
        if not endable: #if user has not found all five items yet
            print 'How adorable!\n'
        else: #if user has found all five items
            print 'Perhaps this is the piece of artwork Rosewater mentioned.'
            print 'It certainly is quite aesthetically pleasing.'
            askContinue()
            print 'As you gaze at the collage, a surge of affectionate emotion overcomes you.'
            print 'Your breath quickens... your heart flutters... and you feel yourself becoming unstuck in time again...'
            office.main(backpack, hp, eggs) #exit room
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

def checkInventory(): #Checks if HP and number of items are within bounds
    global hp
    if len(items) == 5: #user has found all five items
        print 'Congratulations! You have found all three of Weary\'s belongings.'
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
    global items
    items = []
    global hp
    hp = 150
    global woods_grid
    woods_grid = [['' for x in range(5)] for y in range(5)]
    move([0,0]) #restart movement at bed square

def endGame(): #Function to continue narrative once user finds all items
    global endable
    endable = True #allows user to exit room
    
    print '\"Rosewater!\" you exclaim excitedly. \"I found all of your items!\"'
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
    data = [row[:] for row in woods_grid] #copy of zoo_grid
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

def print_backpack(backpack): #Prints list of current backpack contents
    print '\nContents of Backpack:'
    if len(backpack) == 0: #if backpack is empty
        print 'Empty'
    else:
        for i in range (len(backpack)):
            print str(i+1) + ': ' + backpack[i] #print number and item
    print ''
    return

def main(b, h, e): #Function gives background narrative and calls move() for the first time
    #initialize global variables
    global backpack
    backpack = b
    global hp 
    hp = h
    global eggs 
    eggs = e
    global items 
    items = []
    global woods_grid
    woods_grid = [['' for x in range(5)] for y in range(5)]
    global endable
    endable = False
    global drawer
    drawer = True
    #start position
    start = [0, 0]
    
    #narrative
    print '\n***\n'
    print 'The forest is completely silent, save for your laboring breaths.'
    print 'You see a tree up ahead.'
    askContinue() #delays display of text until user chooses to continue
    
    print '-'*100
    print 'It is no different than the hundreds of other trees in this patch of forest.'
    print 'And yet... it is strangely alluring.'
    print 'You approach it hurriedly, unable to resist this feeling of belonging.'
    print 'Somehow, you know this is where you must sit and wait.'
    askContinue()
    
    print '-'*100
    print 'Wait for what, you don\'t know, but you wait anyways.'
    askContinue()
    
    print '-'*100
    print 'You look up at the sky and see that some time has passed.'
    print 'Deeply disappointed, you cast the most upsetting frown you could muster at the tree.'
    print 'The tree frowns back.'
    askContinue()
    
    print '-'*100
    print 'You blink frantically in confusion and the tree vanishes.'
    print 'But the frown is still there. Instead, you realize, your father stands before you.'
    print 'His face contorts with anger and he opens his mouth to shout at you.'
    print 'But all that came out was a melodious tune.'
    askContinue()
    
    print '-'*100
    print 'You open your mouth to respond, but then it occurs to you that you\'re underwater. And you don\'t know how to swim.'
    print 'Chlorinated pool water fills your lungs. The beautiful symphony follows you to the floor of the pool.'
    print 'As the world grows dark, you embrace the darkness eagerly.'
    askContinue()
    
    print '\n***\n'
    
    print 'You wake up in the forest shaking violently. You wonder why you\'re having a seizure.'
    print 'Weary stops shaking you and punches you in the face.'
    print '\"The Three Musketers never leave anyone behind, not even your sorry bum. C\'mon hurry up, we gotta go.\"'
    askContinue()
    
    print '\n***\n'
    
    print '"Oh shoot! I\'ve lost all my precious belongings. This is all your fault! We\'re not leaving until we find my BULLETPROOF BIBLE, TRENCH KNIFE, and GAS MASK.\"'
    print 'Feeling sorry for Weary, you stumble out of your daze and begin shuffling about the forest in search of his belongings.'
    print 'Objective: Find all of Weary\'s belongings to procede to the next stage. Beware, it might be smarter to pick up some items before others.\n'
    
    print 'At any point, you may enter the command \'MAP\' to display a map of the room and the objects you have uncovered.'
    print 'However, doing so will invoke a cost of -25 HP.'
    print 'Choose wisely, and good luck!'
    askContinue() 
    
    print '\n***\n'
    
    move(start) #begin movement