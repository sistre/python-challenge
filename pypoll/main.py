# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


# Module for importing the collections module to use the Counter class
import collections as ct

csvpath = os.path.join('Resources', 'election_data.csv')
txtpath = os.path.join('analysis', 'pypoll_results.txt')

# Reading budget_data.csv using CSV module
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Sets the initial value of the total votes to zero
    votes_total = 0

    # Read each row of data after the header
    votes = ct.Counter()
    reader = csv.reader(csvfile)
    next(reader)
    
    # Count the votes for each candidate
    for line in reader:
        votes_total = votes_total + 1
        candidate = line[-1]
        votes[candidate] += 1

# Sets the range as the number of candidates
ranger = int(len(votes))


# The following two functions pull the data out of the counter dict, calculate the percentage of votes each candidate recieved, and prints or writes the necessary info using a for loop
def talley_votes_term(number):
    for i in votes.most_common(number):
        percent_votes = '%.3f'%((i[1] / votes_total)*100)
        print(f"{i[0]}: {percent_votes}% ({i[1]})")

def talley_votes_txt(number):
    for i in votes.most_common(number):
        percent_votes = '%.3f'%((i[1] / votes_total)*100)
        text.write(f"{i[0]}: {percent_votes}% ({i[1]})\n    ")

# Print election results to the terminal
print(f'''
Election Results
-------------------------
Total Votes: {votes_total}
-------------------------
''')
talley_votes_term(ranger)
print(f'''
-------------------------
Winner: {votes.most_common(1)[0][0]}
-------------------------
''')

# Writes the election results to the txt file
with open(txtpath, 'w') as text:
    text.write(f'''
    Election Results
    -------------------------
    Total Votes: {votes_total}
    -------------------------
    ''')
    talley_votes_txt(ranger)
    text.write(f'''
    -------------------------
    Winner: {votes.most_common(1)[0][0]}
    -------------------------
    ''')
