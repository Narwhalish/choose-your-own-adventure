'''Choose Your Own Adventure: Backpack
Provides access to user's backapck. User can choose to print contents (with quantities),
discard item, and/or use item.
'''

def main(b, h): #Allows user to choose among four actions to perform using backpack
    backpack = b
    hp = h
    dict_backpack = {'breakfast': 0, 'pill': 0, 'bulletproof bible': 0, 'trench knife': 0, 'gas mask': 0, 'broken gas mask': 0,
    'spoon': 0, 'shovel': 0, 'book':0}
    for item in backpack: #convert backpack list to a dictionary with quantities
        dict_backpack[item]+=1
    while True: #loop until user chooses to exit
        print '\nWelcome to your backpack!'
        print '\tTo print contents, enter \'1\'.'
        print '\tTo discard an item, enter \'2\'.'
        print '\tTo use an item, enter \'3\'.'
        print '\tTo exit backpack, enter \'4\'.'
        command = raw_input('Enter your choice: ')
        if command.strip() == '1': #print contents
            print '\nContents of Backpack:'
            output = ''
            for i,v in dict_backpack.iteritems(): 
                if v>0: 
                    output+= '\n\t' + i + ' (Quantity: ' + str(v) + ')' #add item to printed list
            if output == '': #if backpack is empty
                output+='\tEmpty'
            print output
        elif command.strip() == '2': #disard item
            discard = raw_input('\nWhat item would you like to discard? ')
            #check if item is in backpack
            if discard.strip().lower() in dict_backpack and dict_backpack[discard.strip().lower()]>0:
                dict_backpack[discard.lower().strip()]-=1 #remove item 
                print 'Discarded!'
            else:
                print 'Item not in backpack'
        elif command.strip() == '3': #use item
            use = raw_input('\nWhat item would you like to use? ')
            if use == 'pill':
                hp+=15
                if hp>150:
                    hp = 150
                print 'Pill has been used. Add 15 to HP.'
            else: #item not usable
                print 'That item cannot be used.'
        elif command.strip() == '4': #exit
            break
        else: #improper input
            print 'Command not recognized. Try again.'
    new_backpack = []
    for i,v in dict_backpack.iteritems(): #convert dictionary back to list
        for j in range(v):
            new_backpack.append(i)
    return new_backpack, hp