# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Stores the paths for the CSV data and TXT output files
csvpath = os.path.join('Resources', 'budget_data.csv')
txtpath = os.path.join('analysis', 'pybank_results.txt')

# Reading budget_data.csv using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # sets the variables' starting values
    ttl_months = 0
    total = 0
    total_change = 0
    mon_change = 0
    previous_profit = 0
    max_change = 0
    min_change = 0

    # Read each row of data after the header
    for row in csvreader:
        ttl_months = ttl_months + 1
        total += int(row[1])
        
        # Filter out the first month because there is no change
        if previous_profit != 0:
            
            # Calculates the change for the month
            mon_change = int(row[1]) - previous_profit
            
            # Adds the change to the total change
            total_change += mon_change
            
            # Checks to see if a the change is the min value and if so stores the month and the change
            if mon_change < min_change:
                 min_change_mon = str(row[0])
                 min_change = mon_change
            
            # Checks to see if a the change is the max value and if so stores the month and the change
            if mon_change > max_change:
                 max_change_mon = str(row[0])
                 max_change = mon_change


        previous_profit = int(row[1])
    
    average_change = (total_change / (ttl_months-1))
        
# Prints the analysis to the terminal 
print(f'''
Financial Analysis
----------------------------
Total Months: {ttl_months}
Total: ${total}
Average Change: ${round(average_change,2)}
Greatest Increase in Profits: {max_change_mon} ({max_change})
Greatest Decrease in Profits: {min_change_mon} ({min_change})
''')

# Writes the analysis to the txt file
with open(txtpath, 'w') as text:
    text.write(f'''
    Financial Analysis
    ----------------------------
    Total Months: {ttl_months}
    Total: ${total}
    Average Change: ${round(average_change,2)}
    Greatest Increase in Profits: {max_change_mon} ({max_change})
    Greatest Decrease in Profits: {min_change_mon} ({min_change})
    ''')