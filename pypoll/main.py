# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv



import collections as ct

csvpath = os.path.join('Resources', 'election_data.csv')

# Reading budget_data.csv using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    ttl_months = 0
    total = 0

    # Read each row of data after the header
    votes = ct.Counter()
    reader = csv.reader(csvfile)
    next(reader)
    
    # Count the votes for each candidate
    for line in reader:
        candidate = line[-1]
        votes[candidate] += 1
    
print(f'''
    {votes}
    {votes.most_common(1)}
    ''')