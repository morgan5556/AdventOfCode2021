# Advent of Code 2021

This GitHub repository contains all my solutions for [Advent of Code 2021](https://adventofcode.com/). They are written in Python in order to gain more knowledge in the language.

## Day One
My solutions and the puzzle input for Day One can be found in the `day_1` folder.

Challenge 1: 1/1 Star

> I did this challenge by looping through each line in the text file. Setting the 'previousNum' value as 0, and the 'currentNum' as the first line, I then compare these values. After all values have been compared, the 'increases' value is decreased by 1 to account for the 'previousNum' variable being set as 0 at the start.

Challenge 2: 1/1 Star

> I did this challenge by using a while loop to create the measurement values, in which they are stored in a list named 'measurementList'. The loop has a try-except statement to ensure no errors occur if the program tries to find an item in the list that does not exist. After this, the code is similar to that of challenge 1 but instead of going through each line in the text file, it goes through each element in the 'measurementList'.

## Day Two
My solutions and the puzzle input for Day Two can be found in the `day_2` folder.

Challenge 1: 1/1 Star

> I did this challenge by looping through each instruction in the text file and splitting it into a direction and a value. From this, I use an if statement to determine what direction the instruction is. The calculations are done based on the if statement.

Challenge 2: 1/1 Star

> This challenge was done in a similar way to Challenge 1, with the only difference being the change in the calculations made in the if statement.

## Day Three
My solutions and the puzzle input for Day Three can be found in the `day_3` folder.

Challenge 1: 1/1 Star

> I did this challenge by first creating a loop from 0 to 11 to loop over each bit in the binary string. I then looped through each line inside this loop and counted the occurences of 1s and 0s. I then used an if statement to determine how the gamma and epsilon rates should be changed.

Challenge 2: 0/1 Star

> Unfortunatley, I was unable to complete this challenge on December 3rd. My solution can be found in the repository, however, I did not get the correct answer. When testing, it occured that not all the binary strings in the list were deleted if it didn't follow the requirements.