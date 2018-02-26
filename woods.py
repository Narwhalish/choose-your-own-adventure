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
import train

def move(pos): #Accepts user input to move through room
    global woods_grid
    global hp
    position = pos #current position 
    print '-'*100
    if not endable: #whether or not user has found all of Weary's items
        checkVitals() #check to see if HP has been drained or score has been reached
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
            command = raw_input('To inspect it, enter \'1\'. To try to take it, enter \'2\'. To do nothing, enter \'0\': ')
            if command.strip() == '1': #if inspect
                print 'Yep, it\'s really tangled up in there.'
                break
            elif command.strip() == '2' and 'Trench Knife' in items: #if has trench knife and cuts through straps
                if 'Gas Mask' not in items: #if mask not taken yet
                    print '\nYou glance at the heavy trench knife in your hand.'
                    print 'In a glorious bout of ingenuity, you slice through the straps of the gas mask, freeing it from its wooden prison.'
                    print 'The glass lens are all scratched up. You can\'t see anything through them now! Oh well...'
                    items.append('Gas Mask') #add gas mask to list of found items
                else:
                    print 'Just a bunch of cut up fabric and branches.'
                break
            elif command.strip() == '2' and 'Trench Knife' not in items: #if no trench knife
                print 'You tug with all your might on the mask.'
                print 'The mask snaps off its straps. Oh no, the lens are shattered and the mask is warped!'
                items.append('Broken Gas Mask') #add broken gas mask to list of found items
            elif command.strip() == '0': #if do nothing
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
        displayImage('trench_knife.jpg')
        print 'Pick it up?\n'
        if yesorno():
            if 'Trench Knife' not in items: #if knife was not taken yet
                print 'In your haste to grab it, you slice yourself on the blade.'
                print 'You manage to put it away before you hurt yourself more.'
                items.append('Trench Knife') #add trench knife to list of found items
            else:
                print 'How could Weary have dropped this?'
        return
            
    elif (x, y) == (0, 4):
        woods_grid[0][4] = 'Voodoo Doll' #add to map
        print 'An eerie looking doll sits abandoned next to a decaying tree stump.'
        displayImage('voodoo.jpg')
        while True: #loop until user gives proper input
            command = raw_input('To inspect it, enter \'1\'. To try to take it, enter \'2\'. To do nothing, enter \'0\': ')
            if command.strip() == '1': #if inspect
                print 'Something tells you that you shouln\'t look at it directly.'
                print 'But wait, there seems to be a small book laying right next to it.'
                print 'Could it be the bulletproof Bible that Weary lost?'
                break
            elif command.strip() == '2' and 'Gas Mask' in items: #if has gas mask and goes closer
                if 'Bulletproof Bible' not in items: #if bible not taken yet
                    print '\nPutting on the scratched up gas mask so you couldn\'t see the doll, you stumble towards the tree stump.'
                    print 'Feeling around, your hands land on something leathery and brick-shaped.'
                    print 'You hurriedly stuff the bulletproof Bible in your breast pocket and you book it.'
                    items.append('Bulletproof Bible') #add bible to list of found items
                else:
                    print 'Where did the doll go? You could\'ve sworn it was there a moment ago.'
                break
            elif command.strip() == '2' and 'Broken Gas Mask' in items: #if broken gas mask
                print 'You put on the warped gas mask, it barely covering your face.'
                print 'The doll is just in the corner of your eye, and you couldn\'t help but to glance at it.'
                print 'Suddenly a dreadful feeling washes over you.'
                hp-=200 #instantly kill billy
            elif command.strip() == '2': #has no mask at all
                print 'You couldn\'t help but to stare into the beads of the voodoo doll.'
                print 'Much to your surprise, it stared back.'
                print 'Suddenly a dreadful feeling washes over you.'
                hp-=200 #instantly kill billy
            elif command.strip() == '0': #if do nothing
                break
            else:
                print 'Command not recognized. Try again.'
        return
    
    elif (x, y) == (4, 3):
        woods_grid[3][4] = 'German Patrols' #add to map
        print 'Wandering about in search of Weary\'s items, you suddenly bump into a German infantry unit.'
        print 'You stand there, not knowing what to do.'
        print 'One of them picks up his rifle, aims down his sight, and -- BAM! You\'ve been shot right through the heart!'
        print 'The pain keeps you on the ground. You hear the laughter of the soldiers in the background as they set up camp.'
        if 'Bulletproof Bible' in items: #if has bible
            print 'Why aren\'t you dead? Then, you remember that you had placed the bulletproof bible in your left breastpocket.'
            displayImage('bulletproof_bible.jpg')
            hp-=25
            for n, item in enumerate(items):
                if item == 'Bulletproof Bible':
                    items[n] = 'Damaged Bible'
        elif 'Damaged Bible' in items:
            print 'You wisely turn away from the camp and walk the other way before you are noticed.'
        else:
            print 'The world darkens and fades away. Time slips and cracks.'
            print 'This isn\'t how you remembered your death to be like!'
            hp-=200 #instantly kill billy
        return
    
    elif (x, y) == (4, 4):
        woods_grid[4][4] = 'Bear Trap' #add to map
        print 'It\'s a tarp!'
        print 'You managed to release the tarp, but you\'ve hurt yourself.'
        hp-=40
        displayImage('bear_trap.jpg')
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
    
    print '\"Finally! That took you long enough.\"'
    print 'You hand him the items.'
    askContinue()
    print '-'*100
    print 'Weary stares at the holey Bible.'
    print '\"Hey, what happened to my Bible?\"'
    print 'You tell him that you were shot by a German soldier.'
    askContinue()
    print '-'*100
    print '\"Haha! That\'s quite the story. Be grateful that you had my bulletproof Bible with you, or you would have been dead!'
    askContinue()
    print '\n***\n'
    train.main(backpack, hp, eggs)
    

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
    start = [2, 2]
    
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