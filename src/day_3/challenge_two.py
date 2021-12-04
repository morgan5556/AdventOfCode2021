import time
def calcRates():
    # Open puzzle input file
    file = open('input.txt', 'r')

    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)

    # Declare variables used in for loops
    oneCounter = 0
    zeroCounter = 0
    common = ""

    # Loop from 0 to 11 to get each bit in the binary string
    for count in range(0, 12):
        # Iterate through each line
        for line in lines:
            if line[count] == "0":
                zeroCounter = zeroCounter + 1
            elif line[count] == "1":
                oneCounter = oneCounter + 1

        # Determines if 0 or 1 occurs the most
        if zeroCounter > oneCounter:
            common = "0"
        elif oneCounter > zeroCounter:
            common = "1"
        elif oneCounter == zeroCounter:
            common = "1"

        # Goes through each line to check if it meets the requiremens
        for line in lines:
            if line[count] != common:
                lines.remove(line)

        # Resets the counters
        zeroCounter = 0
        oneCounter = 0

    print(lines)

# Runs the function
calcRates()