# Advent of Code 2021

This GitHub repository contains all my solutions for [Advent of Code 2021](https://adventofcode.com/). They are written in Python in order to gain more knowledge in the language.

## Day One
Challenge 1: 1/1 Star
> I did this challenge by looping through each line in the text file. Setting the 'previousNum' value as 0, and the 'currentNum' as the first line I then compare these values. After all values have been compared, the 'increases' value is decreased by 1 to account for the 'previousNum' variable being set as 0 at the start.

Challenge 2: 1/1 Star

> I did this challenge by using a while loop to create the measurement values, in which they are stored in a list named 'measurementList'. The loop has a try-except statement to ensure no errors occur if the program tries to find an item in the list that does not exist. After this, the code is similar to that of challenge 1 but instead of going through each line in the text file, it goes through each element in the 'measurementList'.