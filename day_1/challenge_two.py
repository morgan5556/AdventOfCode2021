def calcIncreases():
    # Open puzzle input file
    file = open('day_1/input.txt', 'r')
    lines = file.readlines()

    # Declare variables for use in the first for loop
    measurementList = []
    count = 0

    # Loop through all measurement windows
    while True:
        try:
            firstVal = lines[count]
            secondVal = lines[count + 1]
            thirdVal = lines[count + 2]
        except:
            break
        
        # Add and store as a measurement
        measurement = int(firstVal) + int(secondVal) + int(thirdVal)
        measurementList.append(measurement)
        count = count + 1

    # Declare variables for use in the for loop
    previousNum = 0
    increases = 0

    # Loop through all the items in the measurement list
    for currentNum in measurementList:
        currentNum = int(currentNum)

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