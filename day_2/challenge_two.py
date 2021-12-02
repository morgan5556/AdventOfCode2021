def calcPositions():
    # Open puzzle input file
    file = open('input.txt', 'r')
    lines = file.readlines()

    # Declare variables used in the for loop
    horizontalPos = 0
    depth = 0
    aim = 0

    # Iterate through each line in the text file
    for line in lines:
        # Split the instructions
        instruction = line.split()
        direction = str(instruction[0])
        value = int(instruction[1])

        # Check the instruction direction
        if direction == "forward":
            horizontalPos = horizontalPos + value
            depth = depth + (aim * value)
        elif direction == "up":
            aim = aim - value
        elif direction == "down":
            aim = aim + value

    # Outputs the values
    print("Horizontal Position: " + str(horizontalPos))
    print("Depth: " + str(depth))
    print("Total: " + str(horizontalPos * depth))

# Runs the function
calcPositions()