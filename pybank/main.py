# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading budget_data.csv using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    ttl_months = 0
    total = 0

    # Read each row of data after the header
    for row in csvreader:
        ttl_months = ttl_months + 1
        total += int(row[1])
        # mon_change = (row + 1)[1] - row[1]
        # total_change += mon_change
        print(int(row + 1)[1])


    ave_change = total_change/ttl_months 
    
    print(f'''
    Financial Analysis
    ----------------------------
    Total Months: {ttl_months}
    Total: ${total}
    Average  Change: ${ave_change}
    ''')