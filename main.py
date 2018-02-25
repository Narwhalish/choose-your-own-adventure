"""
Name: Emily Liu, Bryan Yao, Karena Yan 
Course: CSE 
Assignment: Choose your Own Adventure
Description: Billy Pilgrim -- Lost in Time

Main program for game. start() provides introductory narrative, initializes 
backpackand HP, and calls function for first room.
"""
 
import hospital

def askContinue(): #Delays display of text until user chooses to continue
    while True: #loops until user gives proper input
        command = raw_input('Enter \'C\' to continue: ')
        if command.strip().upper() == 'C': #if user continues
            return
        else:
            print 'Command not recognized. Try again.'

def start(): #Narrates introduction of game
    #initalize variables
    backpack = []
    hp = 150
    eggs = []
    print '\n\nBILLY PILGRIM -- LOST IN TIME\n\n***\n'
    print 'You, Billy Pilgrim, are unstuck in time.'
    print 'You have seen your birth and death many times, and you pay random vists \
    \n to all the events in between.'
    print 'You have no control over where you are going next. You are in a \
    \n constant stage fright because you never know what part of your life \
    \n you are going to have to act in next.'
    askContinue() #delay until user chooses to continue
    
    print '-'*100
    print 'After years of time travel, you are finally sick of it.'
    print 'All you want is to be able to live your life as planned... but someone\
    \nhas been playing with your clocks.'
    print 'Your mission is to find them, and to set your life back to normal.'
    askContinue()
    
    print '-'*100
    print 'Traverse through a series of events in your life in order to find \
    \nwho has been tampering with your sense of time.'
    print 'You are supplied with 150 points and a backpack to store any items\
    \nyou find over the course of your quest (maximum 10).'
    print '\nGood luck -- let\'s begin!'
    askContinue()
    
    hospital.main(backpack, hp, eggs) #call function for first room
    
if __name__ == '___start___':
    start()