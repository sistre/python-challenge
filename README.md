# python-challenge
Python Challenge Homework

Sean Istre

# The assignment
The python-challenge homework assignment involves solving two problems, PyBank and PyPoll, by importing and reading CSV files and outputing the solutions to both the terminal and a text file.

## PyBank
The script in for the PyBank problem reads the "budget_data.csv" from the Resources folder. Then in a single for loop calculates the total months, the net total amount of profit/losses over the entire period, the net change in profit/losses in the entire period, and determines the greatest increase in profits and the greatest decrease in losses. It then uses this data to calculate average of the changes in profit/losses over the entire period. It then prints the results to the terminal and writes them to a text file "pybank_results.txt" in the analysis folder.

## PyPoll
The script in for the PyPoll problem reads the "election_data.csv" from the Resources folder. Then using a for loop and the collections module's counter class to count the total number of votes and the number of votes for each unique candidate, storing it in a dictionary. A "ranger" variable is then created equal to the number of candidates in the dictionary. Two functions are then created to calculate the percentage of the total votes each candidate recieved and then either print it to the terminal or write to a file. Much of this is done with a for loop and .most_common() methond. Finally, the election results containing the total number of votes cast, a complete list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won, and the winner of the election based on popular vote are both printed to the terminal and written to the "pypoll_results.txt" file by using the results of the calculations,   the result of the two fuctions, and another use of the .most_common() methond to display the winning candidate.
