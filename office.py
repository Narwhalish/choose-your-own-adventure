"""
Name: Emily Liu
Choose Your Own Adventure
Billy Pilgrim's Adventure Through Time

Office Room (Too dark to see into)
Goal: 
    
In the slaughterhouse there are:
    Patient (4): Trivia about themselves to gain trust, then you can treat
        1. Daniel Du
        2. Colucci
        3. Sidhu Arakkal 
    Sign - Allows you a view into the future
    Book - Gives you hints on how to treat people
    Owl Optometer - Gives chance to transport to any location in the past
                    But you can only use it once
    Cabinet - 3rd drawer is lamp 
                    
    
** User Notes: Type %matplotlib inline in the kernel before playing game
                All user entries are case-insensitive**
================================================================================
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import woods
import train
import hospital
import zoo

global space, position
space = [[" "]*5 for i in range(5)]

global f_lamp, success, f_book
success = 0
f_lamp = False
f_book = False

global c_treated, d_treated, s_treated
c_treated = False
d_treated = False
s_treated = False

space[4][2]="Entrance"
entrancepos=[4,2]
doorpos = [0,1]
signpos = [3,3]
bookpos = [3,1]
owlpos = [2,2]
cabinetpos = [4,4]
danielpos = [2,1]
coluccipos = [4,0]
sidhupos = [0,4]


global prow, pcolumn, position
prow = 4
pcolumn = 2
x = "YOU"
position = [prow, pcolumn]

global f_lamp, f_book, owl_use
f_lamp = False
owl_use = False
f_book = False

def displayImage(name): #displays the image using matplotlib
    #name is the name of the image file
    image = mpimg.imread(name)
    ax = plt.axes(frameon=False)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    plt.imshow(image)
    plt.show()
    
def make_map(): #updates and prints the map 
    global space, position
        
    print "\n MAP OF OFFICE" 
    color_grid = [['black']*5 for i in range(5)]
    
    pmap = plt.table(cellText=space, cellColours=color_grid,
            cellLoc='center', rowLoc='left', colLoc = 'center',
            loc='center', bbox=None) #table formatting

    pmap.scale(1, 3.65)
    plt.xticks([])
    plt.yticks([])
    table_cells = pmap.properties()['child_artists']
    
    for cell in table_cells:
        cell._text.set_color('white')
        cell.set_edgecolor('white')
    
    plt.show()
    print "HP: " + str(hp) + " / 150" #prints out the HP of the user

def check_continue(): #delays the narration according to user
    a = True
    while (a):
        c = (raw_input("Press C to continue: ")).upper()
        if (c=='C'):
            a = False
            return
        else: 
            print "Please press C." 

def action(): #helps user move around the map 
    global prow, pcolumn, space, position, f_lamp
    a = raw_input('Up, Down, Right, Left, Backpack (U,D,R,L,B): ').upper()
    if ( a == 'U'): #if user wants to move up
        if prow!=0:
            prow=prow-1 #prevent user from going off of map
            position = [prow, pcolumn] 
            if (position==entrancepos or position==doorpos or  
                position==signpos or position==owlpos or
                position==cabinetpos or position==danielpos or 
                position==coluccipos or position==sidhupos or position==bookpos):
                #if user happens to land on one of the positions with an item
                items() #redirects to various other functions
            else:
                if (f_lamp==False): #if user has not yet found lamp
                    print "Nothing here!" 
                    space[prow][pcolumn]=" "
                else:
                    space[prow][pcolumn]=x #prints out 'YOU' to let user know where s/he is
                    make_map() 
                    space[prow][pcolumn]=" " #resets square
        else:
            print "You can't walk through a wall!" 
            action() #calls itself again
    elif (a =='D'): #if user wants to move down
        if prow!=4: #prevents user from going off of map
            prow=prow+1 
            position = [prow, pcolumn]
            if (position==entrancepos or position==doorpos or  
                position==signpos or position==owlpos or
                position==cabinetpos or position==danielpos or 
                position==coluccipos or position==sidhupos or position==bookpos):
                items() #if user lands on item position, redirects to specific function
            else:
                if (f_lamp==False): #if user has not yet found lamp
                    print "Nothing here!"
                    space[prow][pcolumn]=" "
                else:
                    space[position[0]][position[1]]=x
                    make_map()
                    space[prow][pcolumn]=" "
        else:
            print "You can't walk through a wall!"
            action() 
    elif (a =='L'): #if user wants to move left
        if pcolumn!=0: #prevents from going off map
            pcolumn=pcolumn-1
            position = [prow, pcolumn]
            if (position==entrancepos or position==doorpos or  
                position==signpos or position==owlpos or
                position==cabinetpos or position==danielpos or 
                position==coluccipos or position==sidhupos or position==bookpos):
                items() #if user lands on item position
            else:
                if (f_lamp==False): #if user has not yet found lamp
                    print "Nothing here!"
                    space[prow][pcolumn]=" "
                else:
                    space[position[0]][position[1]]=x
                    make_map()
                    space[prow][pcolumn]=" "

        else:
            print "You can't walk through a wall!"
            action() 
    elif (a =='R'): #if user wants to move right
        if pcolumn!=4: #prevents user from going off map
            pcolumn=pcolumn+1
            position = [prow, pcolumn]
            if (position==entrancepos or position==doorpos or  
                position==signpos or position==owlpos or
                position==cabinetpos or position==danielpos or 
                position==coluccipos or position==sidhupos or position==bookpos):
                items() #if user hits item position
            else:
                if (f_lamp==False): #if user has not yet found lamp
                    print "Nothing here!"
                    space[prow][pcolumn]=" "
                else:
                    space[position[0]][position[1]]=x
                    make_map()
                    space[prow][pcolumn]=" "
        else:
            print "You can't walk through a wall!"
            action() 
    elif (a=='B'): #if user wants to see what is in backpack
        print_backpack(backpack) #calls backpack function
        action() #calls itself
    else:
        print "Please enter valid action!" #if user enters an invalid character
        action() 

def entrance(): #if user lands on entrance position, lets user go back to last room
    global success, f_lamp
    a = True
    space[entrancepos[0]][entrancepos[1]]="YOU\nEntrance" 
    if (f_lamp): #if user has found lamp
        make_map()
        space[entrancepos[0]][entrancepos[1]]=="Entrance"
    while (a):
        print "Do you want to leave the office?" 
        d = (raw_input("To leave, press L. To stay, press S: ")).upper()
        if (d =='L'):
            hospital.main(backpack, hp, eggs) #leads to the next room, the hospital
            break
        elif (d == 'S'):
            print "You decided to stay in the office."
            print "Maybe there are more items!"
            break
        else:
            print "\nPlease enter a valid action!\n" #if user enters invalid character

def door(): #when user lands on door function, lets user go to next room if all patients treated
    global success, f_lamp
    a = True
    if (f_lamp==False): #if lamp has not been found, cannot see what item it is
        print "There seems to be something here, but it's too dark to see!"
        return
    elif (f_lamp): #if user found lamp
        space[doorpos[0]][doorpos[1]]="YOU\nDoor"
        make_map()
        space[doorpos[0]][doorpos[1]]="Door"
        print "You found a door!"
        if (success==3): #if all of the patients have been treated
            while (a): 
                print "I wonder where this door leads... Will you open the door?"
                d = (raw_input("To enter, press E. To stay, press S: ")).upper()
                if (d =='E'):
                    zoo.main(backpack, hp, eggs) #enter next room, zoo
                    break
                elif (d == 'S'):
                    print "You decided to stay in the office."
                    print "Maybe there are more items!"
                    break
                else:
                    print "\nPlease enter a valid action!\n" #invalid character 
        else:
            print "Oops! You have to treat all of the patients before leaving!" #
            #if user has not yet treated all of the patients, cannot leave

def sign(): #if user lands on sign position, lets user foresee stuff in future
    global f_lamp
    a = True
    if (f_lamp==False): #if user hasn't found lamp, can't see sign
        print "There seems to be something here, but it's too dark to see!"
        return
    elif (f_lamp):
        space[signpos[0]][signpos[1]]="YOU\nSign"
        make_map()
        space[signpos[0]][signpos[1]]="Sign"
        print "You found a sign!"
        print "It is posted high above the wall in a white frame. You wonder why it's there."
        check_continue() #delays narration
        displayImage('sign.jpg') #display the sign as an image in kernel
        print "It reads: \"God grant me the serenity to accept the things I cannot\
                \nchange, the courage to change the things I can, and wisdom to know\
                \nthe difference.\""
        check_continue() 
        while (a):
            d = (raw_input("Will you take a closer look? Y or N: ")).upper()
            if (d =='Y'): #if user wants to foresee image
                print "You peer closer at the fading ink on the sign. Suddenly, you begin\
                \nto feel kind of drowsy..."
                check_continue()
                print "The world seems to woosh around you, and you make out the blurred image\
                        \nof a timeline of your life. Except...you can see the future!"
                check_continue()
                print "How is this possible? you wonder. But you won't let this chance slip from\
                        \nyou! You must learn who is playing with your clocks, and this opportunity\
                        \nmay be the only way to figure out the mystery."
                print "You can see your memories as they float around you... the woods, the train, Wild\
                        \nBob...and a slaughterhouse?"
                check_continue()
                print "Your vision is getting blurrier by the second, but you refuse to quit \
                        \ntrying. You look around desperately for more places, but all you can\
                        \nmake out are flying shells from exploding bombs and raging fires."
                print "Suddenly, you see the silhouette of a figure -- tall and lean, with a long\
                        \novercoat that seemed to flutter with the ebbing of time."
                check_continue()
                print "His tall hat makes him look more mysterious than he was already, and as he turned \
                        \naround slowly, you could almost just make out his smile..."
                check_continue()
                print "You blink, but the vision is gone. Bewildered, you blink rapidly again, but all you can\
                        \nsee are the black letters of the sign. The vision is nowhere to be found. Sighing,\
                        \nyou back away slowly and look around the room. You couldn't quite catch the man's face, \
                        \nso why did he seem so familiar?"
                return
            elif (d == 'N'): #if user doesn't want to look at sign
                print "You decide not to look at the sign. What use will a plain \
                \nsign be to you anyway?." 
                return
            else:
                print "\nPlease enter a valid action!\n"
   
def owl(): #if user lands on owl position, allows user to select room from past to travel back to
    #however, can only be used once. 
    global f_lamp, owl_use
    a = True
    b=True
    if (f_lamp==False): #if user has no lamp
        print "There seems to be something here, but it's too dark to see!"
        return
    elif (f_lamp):
        space[owlpos[0]][owlpos[1]]="YOU\nOwl"
        make_map()
        space[owlpos[0]][owlpos[1]]="Owl"
        print "You found your owl optometer!" 
        if (owl_use): #if user has already used it
            print "You try to remember how to use the optometer and travel back\
            \ninto the past, but your memory is slipping. You give up."
        elif (owl_use==False): #if user hasn't already used it
            print "The owl optometer's beady eyes stare back at you as if taunting\
            \nyou to change its lens and test your eyesight."
            while (a):
                d = (raw_input("Will you look in? Y or N: ")).upper()
                if (d=='Y'): #if user wants to go back into past
                    print "So you do. But as you press your face into the optometer, you hear \
                    \na dramatic whoosh as you are launched into the cosmos of time."
                    owl_use = True #owl has been used
                    while (b):
                        d = (raw_input("Where would you like to go?\
                                        \na. Woods\
                                        \nb. Train\
                                        \nc. Hospital\
                                        \nAnswer: ")).upper()
                        if (d=='A'): #if user wants to go back to the woods
                            print "You can feel yourself getting dizzier...dizzier..."
                            woods.main(backpack, hp, eggs)
                        if (d=='B'): #if user  wants to go back to the train
                            print "You can feel yourself getting dizzier....dizzier..."
                            train.main(backpack, hp, eggs)
                        if (d=='C'): #if user wants to go back to the hospital
                            print "You can feel yourself getting dizzier...dizzier..."
                            hospital.main(backpack, hp, eggs)
                        else:
                            print "Please enter a valid answer!"
                elif (d=='N'): #if user decides not to look at owl
                    print "You decide that the owl is too creepy for you."
                    return
                else:
                    print "Please enter a valid action!"         
    
def cabinet(): #if user lands on cabinet position, can choose to open the drawers
    #1. old magazine #2. watch #3. lamp
    a = True
    global f_lamp
    space[prow][pcolumn]="YOU\nCabinet"
    print "You found a cabinet!"
    while (a):
        d = (raw_input("Will you look inside? Y or N: ")).upper()
        if (d=='Y'):
            print "You found three drawers!"
            e = (raw_input("Select a drawer to look into (1,2,3): "))
            if (e=='1'): #doesn't have an effect
                print "You found an old magazine! It looks boring so you leave it."
                return
            elif (e=='2'): #doesn't have an effect except symbolism :)
                print "You found a watch! The clock is ticking...ticking...you don't \
                \nhave much time..."
                return
            elif (e=='3'): #user can now see things in office, make_map()
                f_lamp = True
                print "You found a lamp! Now you can see your surroundings!"
                make_map()
                space[cabinetpos[0]][cabinetpos[1]]="Cabinet"
                return
            else:
                print "Please enter a valid drawer!"
        elif (d=='N'): #user decides not to open drawer
            print "You decide not to look into the drawer. Who knows what could be in there?"
            break    
        else: 
            print "\nPlease enter a valid action!\n"

def daniel(): #if user finds patient Daniel Du
    a = True
    global f_lamp, f_book, success, d_treated
    if (f_lamp==False): #if user has no lamp
        print "There seems to be something here, but it's too dark to see."
        return
    if (f_lamp):
        space[danielpos[0]][danielpos[1]]="YOU\nDaniel"
        make_map()
        space[danielpos[0]][danielpos[1]]="Daniel"
        displayImage('daniel.jpg') #display image of Daniel
        print "You found Daniel!"
        if (d_treated == False): #if user has not yet treated Daniel
            print "\"Dr. Pilgrim, help me! This is tragic! I can't believe this is happening!\""
            if (f_book):
                print "Shaken and slightly terrified, you scream, \"What's the matter? Are you going \
                        \nblind?!\""
                check_continue()
                print "When you start screaming, Daniel begins to panic more and begins screaming too.\
                        \n\"No, no, Dr. Pilgrim -- well, yes, I can't seem to see anything -- but I CAN'T\
                        \nSEE JISOO ANYMORE! I CAN'T WATCH HER ON MY PHONE, I CAN'T SEE HER VIDEOS, I CAN'T \
                        \nEVEN FIND THE VOLUME BUTTON TO HEAR HER ANGELIC VOICE!\""
                print "Overwhelmed by his own situation, he plops down on the ground and sobs."
                while (a): 
                    d = (raw_input("Treat Daniel? Y or N: ")).upper()
                    if (d=='Y'): #if user decides to treat Daniel
                        d_treated = True
                        print "Thankfully, the book you found had all of Daniel's symptoms: juvenille progressive\
                                \nblindness, and an affinity for Jisoos?"
                        check_continue()
                        print "Ah. Of course. Stargardt's disease. \"Daniel, with this disease, the afflicted \
                                \nindividuals may not have cures. However, maybe you can discover one in the future! \
                                \nIn regards to your infatuation with Jisoo... Unfortunately, that appears to be a \
                                \nnatural symptom of all Daniels. It appears to be untreatable as well. I recommend\
                                \nyou visit the k-pop specialist, Mr. Sivan Shulman, and/or your counseling agency.\""
                        print "* * * NOTE: Not intended to be used as a diagnosis tool or prescription. * * * "
                        check_continue()
                        print "\"Thank you, Dr. Pilgrim!\" says Daniel. \"I was so worried that I couldn't see Jisoo \
                                \nanymore, but now that I know I can always have someone to talk to, I won't be afraid\
                                \nto face the future without her! I am not afraid, because I am the people's champ!!\""
                        success +=1 #adds +1 patient treated to the count
                        return
                    elif (d=='N'): #if user decides not to treat Daniel
                        print "\"Even you, Dr. Pilgrim? Do you not respect me as the people's champ???\""
                        return
                    else:
                        print "Please type a valid action!"
                else: #if user has not yet found the book 
                    print "\nYou don't seem to know what disease it is! Try looking around the room for \
                    \nyour medical book."
                    return
        else: #if user has already treated Daniel and goes back to position
            print "You already treated Daniel!"
    

def colucci(): #if user lands on patient Colucci 
    a = True
    b = True
    global f_lamp, f_book, success, c_treated
    if (c_treated == False): #if user has not yet treated Colucci
        if (f_lamp==False): #if user cannot see Colucci
            print "There seems to be something here, but it's too dark to see."
            return
        if (f_lamp):
            space[coluccipos[0]][coluccipos[1]]="YOU\nColucci"
            make_map()
            space[coluccipos[0]][coluccipos[1]]="Colucci"
            displayImage('colucci.jpg') #displays image of Colucci
            print "You found Colucci!"
            print "He is floundering around, scratching at his eyes. \"Dr. Pilgrim! \
            \nMy eyes are killing me! They're burning! Please help me!\""
            if (f_book):
                while (a):
                    d = (raw_input("Treat Colucci? Y or N: ")).upper()
                    if (d=='Y'): #if user decides to treat Colucci
                        c_treated = True
                        print "Thankfully, the book you found had all of Colucci's symptoms: itchy eyes,\
                                \na burning sensation, and a feeling of euphoria. The disease?"
                        check_continue()
                        print "\"Colucci, it appears to be that you had prelonged exposure to Adithya. \
                                \nPlease be aware next time that his radiance will damage your retina if \
                                \nyou stare directly at him. You can apply this ointment for your burns.\""
                        check_continue()
                        success +=1 #adds +1 to patient treated count
                        if ('officeadithya' not in eggs): #if user has not yet received an Adithya egg
                            print "\"Thank you, Dr. Pilgrim!\" Colucci exclaims, relieved. \"But before I leave, \
                                    \nplease help me answer this question: "
                            while (b):
                                d = (raw_input("What is Adithya's favorite subject in school? \
                                                \na. English\
                                                \nb. Chemistry\
                                                \nc. VEX\
                                                \nd. History\
                                                \nAnswer: ")).upper()
                                if (d=='C'): #if user answers correctly
                                    eggs.append('officeadithya') #add office Adithya egg to Easter Eggs
                                    print "You made a wild guess and guessed 'VEX'!"
                                    print "\"Congratulations, Dr. Pilgrim!! I can now unashamedly talk to\
                                            \nAdithya! Please accept this egg as a token of my appreciation: "
                                    displayImage('adithya3.jpg') #displays image of Adithya
                                    print "?? It appears to be an Adithya! You don't question his choice of gift\
                                            \nand calmly place it in your pocket."
                                    return
                                elif (d=='A' or d=='B' or d=='D'): #if user answers the wrong answer
                                    print "Colucci looks at you disappointedly and shakes his head. \"A flamingo\
                                            \nwill always be a flamingo.\" You're confused when he walks out the\
                                            \ndoor, refusing to pay you."
                                    return
                                else:
                                    print "Please enter a valid answer!"
                    elif (d=='N'): #if user decides not to treat Colucci
                        print "You decide not to treat Colucci. \"Lucia will hear about this!\" he\
                        \ncries, and runs away."
                        return
                    else:
                        print "Please enter a valid action!"
        else: #if user hasn't found the book yet
            print "\nYou don't seem to know what disease it is! Try looking around the room for \
                    \nyour medical book."
            return
    else: #if user tries to treat Colucci again
        print "You already treated Colucci!"

def sidhu(): #if user lands on patient Sidhu position
    a = True
    global f_lamp, f_book, success, s_treated
    if (f_lamp==False): #if user hasnt' found lamp
        print "There seems to be something here, but it's too dark to see."
        return
    if (f_lamp==True):
        space[sidhupos[0]][sidhupos[1]]="YOU\nSidhu"
        make_map()
        space[sidhupos[0]][sidhupos[1]]="Sidhu"
        displayImage('sidhu.jpg')
        print "You found Sidhu!"
        if (s_treated==False): #if user has not yet treated Sidhu
            print "\"Dr. Pilgrim, help me! My eyes are so painful and I'm seeing spots everywhere.\""
            print "You attempt to shine a flashlight at his face, but that only seems to make it \
                    \nworse. \"Argh! I can't see anymore!\""
            if (f_book):
                while (a):
                    d = (raw_input("Treat Sidhu? Y or N: ")).upper()
                    if (d=='Y'): #if user decides to treat Sidhu
                        s_treated = True
                        print "Thankfully, the book you found had all of Sidhu's symptoms: pain,\
                                \nlight sensitivity, dark spots, and vision loss. The disease?"
                        check_continue()
                        print "\"Uveitis, Sidhu, you have uveitis! How unfortunate. Here, I\
                                \nwill prescribe for you some eye drops to ease inflammation. If it is \
                                \nstill bothering you after a week, well, I am sorry for your loss.\""
                        print "* * * NOTE: Not intended to be used as a diagnosis tool or prescription. * * * "
                        check_continue()
                        print "\"Thank you, Dr. Pilgrim!\" says Sidhu. \"I was so worried that my eyes were looking\
                                \nkind of yucky, but now that I have these eyedrops, I can have eyes that accentuate \
                                \nmy hair!"
                        success +=1 #adds +1 to patient treated count
                        return
                    elif (d=='N'): #if user decides not to treat Sidhu
                        print "Ach!!  Who will treat my eyes now? What if they never match my hair again?"
                        return
                    else:
                        print "Please type a valid action!"
            else: #if user has not yet found the book
                print "\nYou don't seem to know what disease it is! Try looking around the room for \
                        \nyour medical book."
                return
        else:
            print "You already treated Sidhu!"

def book(): #if user lands on book position
    global f_lamp, f_book
    if (f_lamp==False): #if user hasn't found lamp
        print "There's an item, but it's too dark to see!"
        return
    elif (f_lamp): #if user has found lamp 
        if ('book' not in backpack): #if book is not already in backpack
            space[bookpos[0]][bookpos[1]]="YOU\nBook"
            make_map()
            space[bookpos[0]][bookpos[1]]="Book"
            print "You found a book!"
            backpack.append('book') #user can pick up book and put in backpack
            print "Wow. What a heavy book, you think. I wonder what's in it."
            check_continue()
            print "It appears to be a medical dictionary with 1,488 pages of text and \
                    \nsomewhat gruesome images. Just for fun, you look up different eye \
                    \ndiseases, but after skimming over the majority of them, you think \
                    \nagainst it."
            print "It's always nice to have a refresher on your craft as an optometrist,\
                \nyou think, but it can never compare to the Merriam Webster's Dictionary."
        else: #deletes book from the map
            space[bookpos[0]][bookpos[1]]=x
            make_map()
            space[bookpos[0]][bookpos[1]]=" " 

def items(): #redirects user from action() to specific position functions
    decisions = {str(entrancepos): entrance, 
                str(doorpos): door,
                str(signpos): sign,
                str(owlpos): owl,
                str(cabinetpos): cabinet,
                str(danielpos): daniel,
                str(coluccipos): colucci,
                str(sidhupos): sidhu,
                str(bookpos): book}
    decisions[str(position)]()
  
def print_backpack(backpack): #Prints list of current backpack contents
    print '\nContents of Backpack:'
    if len(backpack) == 0: #if backpack is empty
        print 'Empty'
    else:
        for i in range (len(backpack)):
            print str(i+1) + ': ' + backpack[i] #print number and item
    print ''
    return
      
def main(b, h, e): #gets backpack, hp, and eggs from last code
    global success, backpack, hp, eggs
    backpack = b
    hp = h
    eggs = e
    print "\n****************************************************************\n"
    print "The first thing you notice about this room is how quiet it is. The air is \
            \nstiff and still, as if the windows had not been opened for decades. It \
            \nhas a slightly familiar smell, the kind that can only come from a doctor's\
            \noffice. The air was warm and heavy, and you hear your footsteps bounce off \
            \nthe walls of the room. The only thing is that you can't see a single thing."
    check_continue()
    print "\n****************************************************************\n"
    print "The walls of the room appear to close in on you the more you walk around \
            \nthe small space. You bump into various (painfully sharp) objects as you \
            \nfumble in the darkness, reaching vainly for the light switch." 
    check_continue()
    print "\n****************************************************************\n"
    print "You know you are in your optometry office, but you just can't seem to remember\
            \nanything about it. Where was everything? More importantly, why was it so dark??\
            \nThe only way to see what is around you is to search for a flashlight."
    check_continue()
    print "\n****************************************************************\n"
    
    while (success<=3): #while patients have not yet all been treated
        action()
    
    
# if __name__ == '__main__':     (used to test code)
#     main([], 150, [])