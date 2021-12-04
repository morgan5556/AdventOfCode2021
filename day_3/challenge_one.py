def calcRates():
    # Open puzzle input file
    file = open('input.txt', 'r')
    lines = file.readlines()

    # Declare variables used in for loops
    gammaRate = ""
    epsilonRate = ""
    oneCounter = 0
    zeroCounter = 0

    # Loop from 0 to 11 to get each bit in the binary string
    for count in range(0, 12):
        # Iterate through each line
        for line in lines:
            if line[count] == "1":
                oneCounter = oneCounter + 1
            elif line[count] == "0":
                zeroCounter = zeroCounter + 1

        # Determines if 0 or 1 occurs the most
        if zeroCounter > oneCounter:
            gammaRate = gammaRate + "0"
            epsilonRate = epsilonRate + "1"
        elif oneCounter > zeroCounter:
            gammaRate = gammaRate + "1"
            epsilonRate = epsilonRate + "0"

        # Resets the counters
        oneCounter = 0
        zeroCounter = 0

    # Binary to decimal conversion
    gammaRate = int(gammaRate, 2)
    epsilonRate = int(epsilonRate, 2)

    # Calculate power consumption
    powerConsumption = gammaRate * epsilonRate

    # Displays outputs
    print("Gamma Rate: " + str(gammaRate))
    print("Epsilon Rate: " + str(epsilonRate))
    print("Power Consumption: " + str(powerConsumption))

# Runs the function
calcRates()