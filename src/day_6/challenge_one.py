def calcFish():
    # Open puzzle input file 
    file = open('input.txt', 'r')
    lines = file.readlines()

    # Convert file into a list
    initialFish = lines[0]
    fishList = initialFish.split(",")

    # Loop 80 times for the 80 days
    for day in range(1, 81):
        # Go through each fish in the list
        for x in range(0, len(fishList)):
            # Checks if the value is 0, if so it is changed to 6 and 8 is added
            if fishList[x] == 0:
                fishList[x] = 6
                fishList.append(8)
            else:
                # The value is reduced by 1
                fishList[x] = int(fishList[x]) - 1

    # Prints total fish         
    print("Total Fish: " + str(len(fishList)))

# Runs the function
calcFish()