def alignCrabs():
    # Open puzzle input file 
    file = open('input.txt', 'r')
    lines = file.readlines()

    # Convert file into a list of integers
    initialPositions = lines[0]
    crabList = initialPositions.split(",")
    crabList = [int(item) for item in crabList]

    # Find the minimum and maximum values in that list
    minValue = min(crabList)
    maxValue = max(crabList)

    # Declare variables for use in for loop
    currentLowest = 0
    currentDistance = 0

    # Go through each in the range of min and max values
    for value in range(minValue, maxValue + 1):
        for crab in crabList:
            # Calculate the distance between the crab and the current value
            difference = abs(crab - value)

            # Calculate the triangular number where the difference is 'n'
            triangularNumber = (difference * (difference + 1)) // 2
            currentDistance = currentDistance + triangularNumber

        # Sets as the current lowest if it is the lowest
        if currentLowest == 0 or currentDistance < currentLowest:
            currentLowest = currentDistance

        currentDistance = 0

    # Prints out the lowest amount of fuel
    print("The lowest amount of fuel is: " + str(currentLowest))  

# Runs the function
alignCrabs()