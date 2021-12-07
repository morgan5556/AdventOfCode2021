def calcFish():
    # Open puzzle input file 
    file = open('input.txt', 'r')
    lines = file.readlines()

    # Convert file into a list
    initialFish = lines[0]
    fishList = initialFish.split(",")

    # Initialise variables
    zeroCount = 0
    oneCount = 0
    twoCount = 0
    threeCount = 0
    fourCount = 0
    fiveCount = 0
    sixCount = 0
    sevenCount = 0
    eightCount = 0

    for x in range(0, len(fishList)):
        if fishList[x] == "0":
            zeroCount = zeroCount + 1
        elif fishList[x] == "1":
            oneCount = oneCount + 1
        elif fishList[x] == "2":
            twoCount = twoCount + 1
        elif fishList[x] == "3":
            threeCount = threeCount + 1
        elif fishList[x] == "4":
            fourCount = fourCount + 1
        elif fishList[x] == "5":
            fiveCount = fiveCount + 1
        elif fishList[x] == "6":
            sixCount = sixCount + 1
        elif fishList[x] == "7":
            sevenCount = sevenCount + 1
        elif fishList[x] == "8":
            eightCount = eightCount + 1

    # Calculate the number of fish in each group
    print(oneCount)

    # Loop 256 times for the 80 days
    for day in range(2, 81):
        newFish = zeroCount
        zeroCount = oneCount
        oneCount = twoCount
        twoCount = threeCount
        threeCount = fourCount
        fourCount = fiveCount
        fiveCount = sixCount
        sixCount = sevenCount
        sevenCount = eightCount
        eightCount = newFish + zeroCount

        print("Day: " + str(day) + " Total Fish: " + str(zeroCount + oneCount + twoCount + threeCount + fourCount + fiveCount + sixCount + sevenCount + eightCount))

    # Prints total fish         
    print("Total Fish: " + str(zeroCount + oneCount + twoCount + threeCount + fourCount + fiveCount + sixCount + sevenCount + eightCount))

# Runs the function
calcFish()