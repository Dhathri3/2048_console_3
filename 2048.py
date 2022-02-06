import random
# Starts the game
def startGame():
    print ("\n 2048 Console based game.")
    print ("\nYou can move numbers to left, right, top or bottom direction.If you make a 2048 block,you win.\n")
    
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
    loseStatus = 0
    score = 0 # Score of the user
    while True:
        tmp = input("\nTo continue, Press 1 for left, 2 for right, 3 for up, 4 for down movements or\nPress 0 to end the game.\n")
        if tmp in ["1", "2", "3", "4", "0"]:
            dir = direction[tmp]
            if dir == 4:
                print ("\nFinal score: " + str(score))
                break
            else:
                pass
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

# Finds empty slot in the game grid
def findEmptySlot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i, j, 0)
    return (-1, -1, 1)


# Program starts here
startGame()