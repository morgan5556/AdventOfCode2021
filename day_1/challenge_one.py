def calcIncreases():
    # Open puzzle input file
    file = open('day_1/input.txt', 'r')
    lines = file.readlines()

    # Declare variables
    previousNum = 0
    currentNum = 0
    increases = 0

    # Loop through all the lines in the text file
    for line in lines:
        line = line.strip()
        currentNum = int(line)

        # Check if the current number is greater than the previous
        if currentNum > previousNum:
            increases = increases + 1
        
        # Sets the previous number as the current number
        previousNum = currentNum
        
    # Subtract one to count for the first line of the puzzle inpu
    increases = increases - 1

    # Outputs the total number of increases
    print("The total number of increases: " + str(increases))

# Runs the function
calcIncreases()