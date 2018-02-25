'''Choose Your Own Adventure: Boss Battle
Final boss battle of the game. User must correctly answer ten trivia questions
about Slaughterhouse Five to defeat Kurt Vonnegut and win. If the user fails,
return to the beginning of the game.
Leads from: Slaughterhouse
'''

import main 

def askContinue(): #Delays display of text until user chooses to continue
    while True: #loops until user gives proper input
        command = raw_input('Enter \'C\' to continue: ')
        if command.strip().upper() == 'C': #if user continues
            return
        else:
            print 'Command not recognized. Try again.'
            
def getAnswer(): #Function to ask for user input of answer choice
    while True: #loop until user gives proper input
        command = raw_input('Enter answer: ')
        if command.strip().upper() in ['A','B','C','D']: #if proper input
            return command.strip().upper() #return answer choice
        else: #if improper input
            print 'Command not recognized. Try again.'

def trivia(e): #Function to ask user trivia questions
    eggs = len(e) #number of lives 
    while True: #continue until lives run out or until questions finish
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 1:'
        print 'In Chapter 1, Vonnegut sketches the plot of the novel on a piece of wallpaper.'
        print 'What does orange cross-hatching represent?'
        print 'A. Bill\'s abduction'
        print 'B. Mental breakdowns'
        print 'C. Post-war period'
        print 'D. The firebombing'
        if getAnswer() == 'D': #call getAnswer() function
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is D.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 2:'
        print 'What is Ronald Weary\'s position in the army?'
        print 'A. Scout'
        print 'B. Anti-tank gunner'
        print 'C. Foot soldier'
        print 'D. Chaplain'
        if getAnswer() == 'B':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is B.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
    
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 3:'
        print 'What do Weary and Billy\'s captors discover in Weary\'s pocket?'
        print 'A. A cigar'
        print 'B. A photograph'
        print 'C. A small gun'
        print 'D. A silver locket'
        if getAnswer() == 'B':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is B.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 4:'
        print 'What does the arrival of the Tralfamadorian spacecraft sound like?'
        print 'A. A nightingale'
        print 'B. A fox'
        print 'C. A child\'s cry'
        print 'D. An owl'
        if getAnswer() == 'D':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is D.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 5:'
        print 'What does Billy read in his zoo encolsure on the Tralfamadorian planet?'
        print 'A. Valley of the Dolls'
        print 'B. Cinderella'
        print 'C. Slaughterhouse Five'
        print 'D. An optometry magazine'
        if getAnswer() == 'A':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is A.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 6:'
        print 'What color is Billy\'s experience of his death?'
        print 'A. Azure'
        print 'B. Violet'
        print 'C. Ivory'
        print 'D. Red'
        if getAnswer() == 'B':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is B.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 7:'
        print 'What is the name of the mountain that Billy\'s plane crashes into?'
        print 'A. Sugarbush Mountain'
        print 'B. Sugarloaf Mountain'
        print 'C. Sugar Mountain'
        print 'D. Loaf Mountain'
        if getAnswer() == 'A':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is A.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 8:'
        print 'What is Professor Bertram Copeland Rumfoord recovering from?'
        print 'A. A car accident'
        print 'B. A swimming accident'
        print 'C. A skiing accident'
        print 'D. An industrial accident'
        if getAnswer() == 'C':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is C.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 9:'
        print 'In Kilgore Trout\'s book The Big Board, aliens capture an earthlight \
        \nand ask him about which two things?'
        print 'A. Darwin and golf'
        print 'B. Christ and golf'
        print 'C. Darwin and Christ'
        print 'D. Christ and gold'
        if getAnswer() == 'A':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is A.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        
        print '-'*100
        print 'Lives: ' + str(eggs) + '/7'
        print 'Question 10:'
        print 'How does the Maori digger from Dresden die?'
        print 'A. In the firebombing'
        print 'B. Measles'
        print 'C. Dry heaves'
        print 'D. Falling into a pit'
        if getAnswer() == 'C':
            print 'Correct!'
        else:
            print 'Wrong! Correct answer is C.'
            print 'Lose one life.'
            eggs-=1
        if eggs<0:
            break
        askContinue()
        break
    
    return eggs #return number of lives remaining
            
def narrate(e): #Function to narrate end of game
    print '\n***\n'
    
    print 'You exit the Dresden slaughterhouse, slightly wary of what awaits you.'
    print 'The sight is unlike anything you could have imagined.'
    askContinue() #delay until user chooses to continue
    
    print '-'*100
    print 'The sky is black with smoke. Dresden is like the moon now-- nothing but minerals.'
    print 'Everybody in the neighborhood is dead.'
    askContinue()
    
    print '-'*100
    print 'You stumble through the streets, the world in mournful silence around you.'
    print 'Your heart begins to thump. You can hardly even breathe...'
    askContinue()
    
    print '-'*100
    print 'Then, in the distance, you spot a lone figure at the end of the road.'
    print 'You quicken your pace to catch up to them.'
    print '\"Wait up! Who are you? Who\'s been playing with my clocks?\"'
    askContinue()
    
    print '-'*100
    print 'The figure turns around, slowly.'
    print '\"Hello. I see you\'ve finally found me.\"'
    askContinue()
    
    print '-'*100
    print 'You stare at him, dumbfounded.'
    print '\"You... you know who I am? Have you been playing with my clocks. Why am I here? How do I get home?\"'
    print 'The questions rush from your mouth, an unstoppable river of scattered, desperate thoughts.'
    askContinue()
    
    print '-'*100
    print 'He chuckles.'
    print '\"Ah, Billy Pilgrim. The truth? My name...'
    askContinue()
    print 'is'
    askContinue()
    print 'that'
    askContinue()
    print 'which'
    askContinue()
    print 'is'
    askContinue()
    print 'known'
    askContinue()
    print 'as'
    askContinue()
    print '.'
    askContinue()
    print '.'
    askContinue()
    print '.'
    askContinue()
    print 'KURT VONNEGUT.'
    askContinue()
    print 'And you? You are my creation.\"'
    askContinue()
    
    print '-'*100
    print 'You blink without understanding.'
    print '\"What the chinese? Your creation? All I want is for my dang clocks \
    \nto stop hiking and take a rest so that I can cry and die in peace.\"'
    askContinue()
    
    print '-'*100
    print 'He laughs again.'
    print '\"Billy Pilgrim, you truly are my creation. A mere chracter I crafted \
    \nto complement the plot of my latest novel. If you want me to fix your clocks...\
    \nyou will have to convince me to do so.\"'
    askContinue()
    
    print '-'*100
    print '\"What?! How do I do that?\"'
    askContinue()
    
    print '-'*100
    print 'He winks. \"Let\'s have a boss battle... TRIVIA VERSION!!\"'
    askContinue()
    
    print '\n***\n'
    
    print 'To defeat Kurt Vonnegut, you must successfully answer 10 questions \
    \nabout his latest novel, Slaughterhouse Five.'
    askContinue()
    
    print '-'*100
    print 'Remember those figurines you might have collected in the various rooms?'
    print 'Those are bonus lives! For each life, you will be excused one incorrect answer.'
    askContinue()
    
    print '-'*100
    print 'Let\'s begin!'
    
    print '\n***\n'
    
    eggs = trivia(e) #call trivia() function
    if eggs < 0: #if user ran out of lives
        print '\n***\n'
        print 'Oh no! You have run out of lives and lost the boss battle.'
        print 'Kurt Vonnegut laughs once again.'
        askContinue()
        
        print '-'*100
        print '\"Did you really think you could beat me? I\'m sorry, Billy Pilgrim, \
        \nbut I fear you are my character to control. Let\'s turn back the clocks \
        \nagain, shall we?\"'
        askContinue()
        
        print '-'*100
        print 'He ignores your screams of protest, and you feel yourself becoming \
        \nunstuck in time... all the way back to the beginning.'
        main.start() #restart game
    else: #if user completed questions
        print '\n***\n'
        print 'Congratulations! You have won the boss battle!'
        print 'Kurt Vonnegut chuckles, admitting defeat.'
        askContinue()
        
        print '-'*100
        print '\"Well done, Billy Pilgrim. You are sharper than I expected. \
        \nIn reward, I suppose I shall tell you the truth about the clocks.\"'
        askContinue()
        
        print '-'*100
        print 'You nod eagerly, leaning forward in anticipation.'
        print 'Finally-- you can go home!'
        askContinue()
        
        print '-'*100
        print '\"The truth is...\"'
        askContinue()
        print '...'
        askContinue()
        print '...'
        askContinue()
        print '...'
        askContinue()
        
        print '\n***\n'
        print 'Mr. Hanas looks up from his computer, slightly annoyed by the \
        \nboisterous chatter coming from the back of the classroom.'
        print '\"Kurt Vonnegut, get back to coding!\"'
        
        print '\n***\n'
        print 'AND SO IT GOES'