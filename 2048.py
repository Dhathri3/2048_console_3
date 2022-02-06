import random
# Starts the game
def startGame():
    print ("\n 2048 Console based game.")
    print ("\nYou can move numbers to left, right, top or bottom direction.If you make a 2048 block,you win.\n")
    loseStatus = 0
    winStatus=0
    
    # Create the game grid 
    # The game should work for square grid of any size though. I am taking 4*4 grid here.
    grid = [['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.']]
    #This grid will initially have two cells populated at random with a 2 or 4.

    num1 = random.randint(1, 2) * 2
    num2 = random.randint(1, 2) * 2
    i1 = random.randint(0, 3)
    j1 = random.randint(0, 3)
    grid[i1][j1]=str(num1)
    i2 = random.randint(0,3)
    j2 = random.randint(0,3)
    l=0
    if grid[i2][j2] != '.':
        i2, j2, l = findEmptySlot(grid)
    if not l: grid[i2][j2] = str(num2)

    direction = {'1': 0, '4': 1, '2': 2, '3': 3, '0': 4}

    printGrid(grid)
    
    move.score = 0 # Score of the user
    while True:
        tmp = input("\nTo continue, Press 1 for left, 2 for right, 3 for up, 4 for down movements or\nPress 0 to end the game.\n")
        if tmp in ["1", "2", "3", "4", "0"]:
            dir = direction[tmp]
            if dir == 4:
                print ("\nFinal score: " + str(move.score))
                break
            else:
                grid,winStatus = move(grid, dir ,winStatus)
                if (winStatus==1):
                    printGrid(grid)
                    print("You won the game!!!")
                    print ("Final score: " + str(move.score))
                    break
                else:
                    grid, loseStatus= addNumber(grid)
                    printGrid(grid)
                    if loseStatus:
                        print ("\nGame Over")
                        print ("Final score: " + str(move.score))
                        break
                    print ("\nCurrent score: " + str(move.score))
        else:
            print ("\nInvalid direction, please provide valid movement direction (1, 2, 3, 4).")
    return 0


# Prints the current game state
def printGrid(grid):
    print ("\n")
    for i in range(len(grid)):
        res = "\t\t"
        for j in range(len(grid[i])):
            for _ in range(5 - len(grid[i][j])): res += " "
            res += grid[i][j] + " "
        print (res)
        print ("\n")
    return 0

# Adds a random number to the grid
def addNumber(grid):
    num = random.randint(1, 2) * 2
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    lost = 0
    if grid[x][y] != '.':
        x, y, lost = findEmptySlot(grid)
    if not lost: grid[x][y] = str(num)
    return (grid, lost)

# Finds empty slot in the game grid
def findEmptySlot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j, 0)
    return (-1, -1, 1)

# Implements game logic 
# Generalized for all four directions using rotation logic
def move(grid, dir,winStatus):
    for i in range(dir): grid = rotate(grid) #we will be rotating the grid based on direction movement.
    for i in range(len(grid)):
        temp = []
        for j in grid[i]:
            if j != '.':
                temp.append(j)
        temp += ['.'] * grid[i].count('.') 
        for j in range(len(temp) - 1):
            if temp[j] == temp[j + 1] and temp[j] != '.' and temp[j + 1] != '.': #checks if adjacent cells are same
                temp[j] = str(2 * int(temp[j]))
                if(int(temp[j])==2048): #checks whether the sum leads to 2048(check for 4096 if that's the requirement).If yes, win status is set to 1.
                    winStatus=1
                move.score += int(temp[j])
                temp[j + 1] = '.'
        grid[i] = []
        for j in temp:
            if j != '.':
                grid[i].append(j)
        grid[i] += ['.'] * temp.count('.')
    for i in range(4 - dir): grid = rotate(grid)
    return grid,winStatus

# Rotates a 2D list clockwise
def rotate(grid):
    return list(map(list, zip(*grid[::-1])))

# Program starts here
startGame()