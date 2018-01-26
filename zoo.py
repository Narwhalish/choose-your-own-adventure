def move(pos):
    position = pos
    print 'Enter \'R\' to move right'
    print 'Enter \'L\' to move left'
    print 'Enter \'U\' to move up'
    print 'Enter \'D\' to move down'
    while True:
        command = raw_input('\n').strip().upper()
        if command == 'R':
            if position[0]<4:
                position[0]+=1
                break
            else: 
                print 'Cannot move right. Try again.'
        elif command == 'L':
            if position[0]>0:
                position[0]-=1
                break
            else: 
                print 'Cannot move left. Try again.'
        elif command == 'U':
            if position[1]>0:
                position[1]-=1
                break
            else: 
                print 'Cannot move up. Try again.'
        elif command == 'D':
            if position[1]<4:
                position[1]+=1
                break
            else: 
                print 'Cannot move down. Try again.'
        else:
            print 'Invalid input. Please try again.'
    print position
    action(position)

def action(position):
    x, y = position[0], position[1]
    print zoo_grid[position[0]][position[1]]
    move(position)
    
global zoo_grid
zoo_grid = []
for i in range(0,5):
    zoo_grid.append([])
    for j in range(0,5):
        zoo_grid[i].append([''])

start = [0, 0]

print 'Tralfamadorian Zoo :]'
zoo_grid[1][1] = 'You have discovered a wild Montana Wildhack.'
zoo_grid[2][2] = 'You have discovered a wild giraffe.'
zoo_grid[3][3] = 'A wild Tralfamadorian has discovered you. You are now dead.'
zoo_grid[4][4] = 'You have discovered a continental breakfast. Yum!'
move(start)
