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

> I unfortunately did not complete this challenge. I hope to return to it later on during Advent of Code. Any updates will be made here.

## Day Four
My solutions and the puzzle input for Day Four can be found in the `day_4` folder.

Challenge 1: 0/1 Star

> I unfortunately did not complete this challenge. I hope to return to it later on during Advent of Code. Any updates will be made here.

Challenge 2: 0/1 Star

> I unfortunately did not complete this challenge. I hope to return to it later on during Advent of Code. Any updates will be made here.

## Day Five
My solutions and the puzzle input for Day Five can be found in the `day_5` folder.

Challenge 1: 0/1 Star

> I unfortunately did not complete this challenge. I hope to return to it later on during Advent of Code. Any updates will be made here.

Challenge 2: 0/1 Star

> I unfortunately did not complete this challenge. I hope to return to it later on during Advent of Code. Any updates will be made here.

## Day Six
My solutions and the puzzle input for Day Six can be found in the `day_6` folder.

Challenge 1: 1/1 Star

> I did this challenge by creating a for loop that loops from 1 to 80. In that for loop, I loop over every element and subtract 1, if that value is a 0, the element is changed to an 8 and a 6 appended to the list.

Challenge 2: 0/1 Star

> I unfortunately did not complete this challenge. I hope to return to it later on during Advent of Code. Any updates will be made here.

## Day Seven
My solutions and the puzzle input for Day Seven can be found in the `day_7` folder.

Challenge 1: 1/1 Star

> I did this challenge by finding the min and max value in the list and then looping through every value between them. In that loop, the difference between each crab and the value is calculated and added to a 'currentDistance' variable. At the end, it is compared to the 'currentLowest' value.

Challenge 2: 1/1 Star

> I did this challenge in a similar way to challenge 1. Instead of using the 'difference' variable to add to the 'currentDistance' variable, I instead used this as 'n' in the triangular number sequence. This value was added to the 'currentDistance' variable instead.