import hospital

"""
Name: Emily Liu, Bryan Yao, Karena Yan 
Course: CSE 
Assignment: Choose your Own Adventure
Description: Billy Pilgrim's Adventure Through Time
"""

def start():
    backpack = []
    hp = 150
    eggs = []
    print '\n\nBILLY PILGRIM -- ADVENTURE THROUGH TIME\n\n'
    #insert backstory
    hospital.main(backpack, hp, eggs)
    
if __name__ == '___start___':
    start()