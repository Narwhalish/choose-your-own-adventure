'''Choose Your Own Adventure: Zoo
Code for the zoo room. User must make choices to achieve target score before 
being able to exit. Must achieve score before running out of HP. 
Leads from: Office
Leads to: Slaughterhouse
Objects:
    Bathroom
    Bed
    Montana Wildhack
    Television
    Refrigerator
    Microwave
    Tralfamadorian
'''

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import slaughterhouse

def move(pos): #Accepts user input to move through room
    global zoo_grid
    global hp
    global score
    position = pos #current position 
    print '-'*100
    if not endable:
        checkVitals() #check to see if HP has been drained or score has been reached
        print 'Current score: ' + str(score) + '/50'   
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
        elif command == 'BACKPACK': 
            print_backpack(backpack) #call function to print backpack contents
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
    global score
    global fridge
    global leaked
    global brushed
    global embraced
    global story
    global endable
    
    #check if user's position is occupied by an interactive object
    if (x, y) == (0, 2):
        zoo_grid[2][0]='Fridge' #add to map
        print 'You have found the refrigerator. Would you like to open it?\n'
        
        if yesorno(): #asks yes-or-no question
            if fridge: #if fridge is unopened, prompt user action
                print 'There is a continental breakfast in the fridge. How convenient!'
                displayImage('breakfast.jpg') #print image to kernel
                print 'Would you like to take a bite of the continental breakfast?\n'
                if yesorno():
                    print 'You take a bite eagerly, only to find that cold \
                    \nmuffins and danishes do not taste very good.'
                    print 'Loss of 10 HP points.\n'
                    if not endable: #if user hasn't reached target score yet
                        print 'The Tralfamadorians, though, are somewhat amused by your disgust.'
                        print 'Add 5 audience satisfaction points.'
                        print 'Disheartened, you toss the breakfast into the trash and continue.\n'
                        score+=5
                        
                    #update hp, global state of fridge
                    hp-=10
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
        displayImage('microwave.jpg')
        if yesorno():
            if 'breakfast' in backpack: #if user carries breakfast, allow them to use microwave
                print 'You microwave your continental breakfast. Yum! Toasty muffins and danishes.'
                print 'Add 50 HP points.\n'
                if not endable:
                    print 'The Tralfamadorians are fascinated by this strange \
                    \ndevice and its magical warming powers.'
                    print 'Add 10 audience satisfaction points.\n'
                    score+=10
                #update hp, global state of backpack
                hp+=50
                backpack.remove('breakfast')
            else: #if user doesn't have breakfast, print message
                print 'You don\'t have anything to microwave.'
        return
        
    elif (x, y) == (4, 0):
        zoo_grid[0][4]='Bed'
        print 'You have found the bed. Take a quick nap?\n'
        displayImage('bed.JPG')
        if yesorno():
            print 'You hop in and snooze for a while.'
            print 'Add 50 HP points.\n'
            if not endable:
                print 'The Tralfamadorians, however, are bored by your state of torpor.'
                print 'Loss of 15 audience satisfaction points.\n'
                score-=15
            #update hp
            hp+=50
        return
        
    elif (x, y) == (2, 0):
        zoo_grid[0][2]='Bathroom'
        print 'You have found the bathroom. Enter?\n'
        displayImage('bathroom.jpg')
        if yesorno():
            print 'Delightful! The room is a pleasant mint green, furnished with\
            \nappliances from the Sears Roebuck warehouse in Iowa City, Iowa.'
            #loop until user gives proper input
            while True:
                command = raw_input('To brush teeth, enter \'1\'. To take a leak, enter \'2\': ')
                if command.strip() == '1': #to brush teeth
                    if brushed: #if user has already brushed
                        print 'The Tralfamadorian crowd, having already seen\
                        \nthis performance, is underwhelmed.\n'
                        if not endable:
                            print 'Add 5 measly audience satisfaction points.\n'
                            score+=5
                    else: #if user has not brushed yet
                        print 'The Tralfamadorians are intrigued by the strange,\
                        \nbristly stick with which you rub your teeth.\n'
                        if not endable:
                            print 'Add 15 audience satisfaction points.\n'
                            score+=15
                        brushed = True
                    break
                elif command.strip() == '2': #to take a leak
                    if leaked: #if user has already taken a leak
                        print 'The Tralfamadorian crowd, having already seen\
                        \nthis performance, is underwhelmed.\n'
                        if not endable:
                            print 'Add 5 measly audience satisfaction points.\n'
                            score+=5
                    else: #if user has not taken a leak yet
                        print 'The Tralfamadorian crowd goes wild at your display!\n'
                        if not endable:
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
        displayImage('montana.jpg')
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
                        print 'Loss of 15 HP.\n'
                        if not endable:
                            print 'The Tralfamadorians find the crude display of violence extremely unpleasant.'
                            print 'Loss of 10 audience satisfaction points.\n'
                            score-=10
                        hp-=15
                    else: #if user has not embraced yet
                        print 'The Tralfamadorian crowd is delighted, and so is Montana.\n'
                        if not endable:
                            print 'Add 15 audience satisfaction points.\n'
                            score+=15
                        embraced = True
                    break
                elif command.strip() == '2': #to tell a story
                    print '\nYou tell Montana about the bombing of Dresden and\
                    \nhow the four guards, in their astonishment and grief, resembled a barber-shop quartet.'
                    if story: #if user has already told story
                        print 'The Tralfamadorians are quickly bored by the sound of human speech.\n'
                        if not endable:
                            print 'Loss of 5 audience satisfaction points.\n'
                            score-=5
                    else: #if story has not told story yet
                        print 'The Tralfamadorians find the story underwhelming and \"very human\".'
                        print 'However, they do enjoy hearing the strange noises of human speech.\n'
                        if not endable:
                            print 'Add 10 audience satisfaction points.\n'
                            score+=10
                        story = True
                    break
                else:
                    print 'Command not recognized. Try again.'
        return
        
    elif (x, y) == (3, 3):
        zoo_grid[3][3]='Television'
        print 'You have found the television, currently frozen on a western action film. Press play?\n'
        displayImage('television.jpg')
        if yesorno():
            print 'You press the play button. Nothing happens.'
            print 'Press it again?\n'
            if yesorno(): #if user presses button twice
                print '\nConfused, you press the button again. Still nothing.'
                print 'You proceed to slam your fists at the screen and holler until you realize that the TV is nonfunctional.'
                print 'The image of one cowboy killing another is merely pasted to the screen!'
                print 'Mentally and physically drained, you proceed to cry for several hours.'
                print 'Loss of 25 HP.\n'
                if not endable:
                    print 'The Tralfamadorians, though, find your stupidity to be quite entertaining.'
                    print 'Add 15 audience satisfaction points.\n'
                    score+=15
                hp-=25
            else: #if user presses button only once
                print '\nYou intelligently deduce that the TV is nonfunctional.'
                print 'The image of one cowboy killing another is merely pasted to the screen!'
                print 'Filled with pride for your overwhelming logical reasoning skills, your mood is much improved.'
                print 'Add 15 HP points.\n'
                hp+=15
        return
        
    elif (x, y) == (2, 2):
        zoo_grid[2][2]='Tralfamadorian'
        print 'You have found a Tralfamadorian in your room!'
        displayImage('tralfamadorian.jpg')
        print 'Speak to it?'
        if yesorno(): #if user wants to speak
            if 'zooadithya' not in eggs: #if user has not received adithya yet
                print '\"Hello,\" it says. \"I have but a single question for you-- what is your favorite shape?\"'
                while True: #loop until user gives proper input
                    print '\nFor \'triangle,\' enter 0.'
                    print 'For \'square,\' enter 1.'
                    print 'For \'circle,\' enter 2.'
                    print 'For \'pentagon,\' enter 3.'
                    command = raw_input('What would you like to choose? ')
                    if command.strip() == '1': #if correct answer
                        print '\nThe Tralfamadorian blinks rapidly, as if in excitement.'
                        print '\"Excellent!\" it exclaims. \"Mine is a square as well. Here, take this as a token of my gratitude.\"'
                        print 'The Tralfamadorian hands you a small figurine of a very comely young man.'
                        displayImage('adithya1.jpg')
                        print 'You are not sure of its purpose, but you accept the gift nonetheless and continue on your journey.\n'
                        eggs.append('zooadithya') #add figurine to list of adithyas
                        break
                    elif command.strip() in ('0','2','3'): #if incorrect answer
                        print '\nThe Tralfamadorian closes its eye in disappointment.'
                        print '\"How unfortunate,\" it muses. \"Carry on, then.\"'
                        print 'Confused, you turn away and continue on your journey.\n' 
                        break
                    else: 
                        print 'Command not recognized. Try again.'
            else: #if user has already received adithya
                print 'The Tralfamadorian recognizes you and blinks happily.'
                print '\"Hello! It was very pleasant speaking to you before. I am quite busy now, though. No time for chit chat!\"'
                print 'You leave it to its work and continue on your journey.\n'
        else:
            print 'You ignore the Tralfamadorian and continue on your journey.\n'
        return
        
    elif (x, y) == (4, 2):
        if endable: #if user has already reached target score
            print 'You have found the time portal!'
            print 'Congratulations-- you have completed this chapter!'
            print 'Thankful that you no longer have to deal with the Tralfamadorians,\
            \nyou hop through the portal and travel to Dresden, 1945.'
            print '\n***\n'
            slaughterhouse.main(backpack, hp, eggs)
        else: #if user has not yet reached target score
            print 'Hmmm... there\'s something strange about the wall here, but\
            \nyou can\'t seem to discern what that might be.'
            print 'Oh well!\n'
            return
            
    else: #if user's position is unoccupied
        print 'Nothing here.\n'
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

def checkVitals(): #Checks if HP and score values are within bounds
    global score
    global hp
    if score < 0: #negative score
        score = 0
    if score >= 50: #score met 
        print 'Congratulations! You have successfully satisfied your audience.'
        print 'Your total score is: ' + str(score)
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

def endGame(): #Function to continue narrative once user reaches target score
    global endable
    endable = True #allows user to exit room
    global hp
    
    print '\"Thank you Billy Pilgrim,\" a Tralfamadorian says through the zoo loudspeaker.'
    print '\"That was an inspiring performance. Nicely done.\"'
    askContinue()
    print '-'*100
    print '\"Now will you tell me who\'s been playing with the clocks?\" you demand.'
    askContinue()
    print '-'*100
    print '\"Why would I do that?\" The Tralfamadorian makes a noise that vaguely resembles laughter.'
    print '\"All I can do is give you a hint.\"'
    askContinue()
    print '-'*100
    print '\"What! You said you\'d tell me,\" you scream in outrage.'
    askContinue()
    print '-'*100
    print '\"I most certainly did not. I said I could help you, and help you I shall.\"'
    print '\"The person playing with the clocks? You can find them in Dresden, 1945.\"'
    askContinue()
    print '-'*100
    print '\"Dresden... how do I get there?\" you ask.'
    askContinue()
    print '-'*100
    print '\"I can create a time portal for you. I\'m afraid you\'ll have to find it in the zoo yourself, though.\"'
    print 'The Tralfamadorian makes the laughing sound again, then clicks off the loudspeaker.'
    print 'You scream in spiteful frustration, wondering why all the bad things in life have to happen to you.'
    askContinue()
    print '-'*100
    print 'You have now been returned to your starting square, and your HP has been restored.' 
    print 'However, as before, each step uses up valuable HP. If you run out before finding the portal, you will be forced to restart.'
    print 'Good luck!' 
    askContinue()
    print '\n***\n'
    
    hp = 150 #reset hp
    move([0,0]) #restart at original square
    
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

def reset(): #Resets default values of global variables
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
    move([4, 0]) #restart movement at bed square

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
    global score
    score = 0
    global zoo_grid
    zoo_grid = [['' for x in range(5)] for y in range(5)]
    global fridge
    global leaked 
    global brushed
    global embraced
    global story
    global endable
    fridge, leaked, brushed, embraced, story, endable = True, False, False, False, False, False
    
    #start position
    start = [0, 0]
    
    #narrative
    print '\n***\n'
    
    print 'You wake up, delirious and foggy-eyed.'
    print 'It is strangely cold, and upon looking down, you realize that you are completely naked.'
    print '\"Oh no,\" you think to yourself. \"Not again.\"'
    askContinue() #delays display of text until user chooses to continue
    
    print '-'*100
    print 'It is the year 1967.'
    print 'You are on the Planet Tralfamadore, on exhibit in a Tralfamadorian Zoo.'
    print 'Strange as it may seem, this isn\'t the first time you\'ve been abducted.'
    print 'The Tralfamadorians love to study the human body, and they consider\
    \nyou to be a prime specimen (largely because they don\'t know any better).\n'
    print 'This time, though, you are fed up with their antics.'
    askContinue()
    
    print '-'*100
    print '\"Why am I here again?\" you shout, hoping that someone is around to hear you.'
    print 'A Tralfamadorian appears to your right. \"Such a human thing to say.\"'
    askContinue()
    
    print '-'*100
    print 'You feel somewhat offended, but ignore the cheeky comment.'
    print '\"I\'m tired of being unstuck in time,\" you whine. \"Who\'s been playing with the clocks? Is it you?\"\n'
    print '\"Nonsense. Do you think I care that much about you?\"'
    askContinue()
    
    print '-'*100
    print '\"Will you at least let me go?\" you plead.\n'
    print 'The Tralfamadorian pauses in consideration. \"Perhaps. But you must entertain the crowd first.\"'
    askContinue()
    
    print '-'*100
    print '\"But I don\'t want to entertain the crowd. I want to go home.\"'
    askContinue()
    
    print '-'*100
    print 'The Tralfamadorian chuckles. \"Humans and their obsession with free will. So amusing.\"'
    print '\"But no, Billy Pilgrim, you will have to stay a while. If you perform well, I can even help you.\"'
    print '\"Someone is, in fact, playing with the clocks. And I happen to know who that someone might be.\"'
    askContinue()
    
    print '\n***\n'
    
    print 'In order to return to Earth, you must entertain the Tralfamadorians!'
    print 'Travel around the zoo and interact with objects in an effort to elevate your audience satisfaction score.'
    print 'Don\'t dilly dally too much, though. Each step you take uses up valuable HP.'
    print 'If you run out of HP, you will be forced to sleep and restart this chapter of the game.\n'
    
    print 'At any point, you may enter the command \'MAP\' to display a map of the zoo and the objects you have uncovered.'
    print 'However, doing so will invoke a cost of -25 HP.'
    print 'Choose wisely, and good luck!'
    askContinue()
    
    print '\n***\n'
    
    move(start) #begin movement