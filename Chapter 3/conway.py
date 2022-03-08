# Conway's Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] #create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Add a living cells
        else:
            column.append(' ') # Add a dead cells
    nextCells.append(column) # nextCells is  a list of colum lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # Print a newline at the end of the row.

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neighbor:
            numNeigbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
               numNeigbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
               numNeigbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
               numNeigbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
               numNeigbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
               numNeigbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
               numNeigbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
               numNeigbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
               numNeigbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeigbors == 2 or numNeigbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells == ' ' and numNeigbors == 3:
                # Dead ceels with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                #Everything else dies or stay dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add 1-second pause to reduce flickering
