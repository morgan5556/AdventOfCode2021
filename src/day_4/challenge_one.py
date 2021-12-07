def bingoCounter():
    # Open puzzle input file 
    file = open('input.txt', 'r')
    lines = file.readlines()

    # Split the puzzle input into a list
    bingoList = lines[0].split()

    # Iterate through all the numbers in the list
    for currentNumber in bingoList:
        for x in range(2, len(lines)):
            numberList = lines[x].split()

            if numberList == []:
                continue

            for number in numberList:
                if number == currentNumber:
                    numberList[number] == "X"
            listString = ' '.join(str(item) for item in numberList)
            lines[x] = listString

    for x in range(2, len(lines)):
        print(lines[x])

bingoCounter()