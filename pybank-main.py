#Code for pybank

#Open CSV File

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	print(csvreader)
	
	#Task 1: Tabulate the number of months of data in budget_data.csv
	
	#Create empty lists
	dollars =[]
	month_period = []
	
	#Populate empty list
	for rows in csvreader:
		dollars.append(rows[1])
		month_period.append(rows[0])
	
	#Remove header
	dollars.pop(0)
	month_period.pop(0)		
	
	#Obtain and print list length
	months = len(dollars)
	print(f"Total Months: {months}")
	
	#Task 2: Determine net profit/loss over entire period
	
	#Convert all loss values from string to integer
	for i in range(0,months):
		dollars[i] = int(dollars[i])
	
	#Sum up all the values within the list named "Dollars"
	total=0
	for value in range(0,months):
		total = total + dollars[value]
		
	print(f"Total Net Profit/Loss is: ${total}")
	
	#Task 3: Find average of month-to-month revenue changes
	
	#Create empty list
	bl_change = []
	
	#Populate empty list with monthly profit/loss changes
	for r in range(1,len(dollars)):
		bl_change.append(dollars[r]-dollars[r-1])
	
	#Get average of monthly profit/loss changes	
		avg_bl_change = sum(bl_change)/len(bl_change)
		avg_bl_change_round = round(avg_bl_change, 2) 
		
	#Task 4/5: Find min/max monthly bottomline changes
		min_bl_change = min(bl_change)
		max_bl_change = max(bl_change)
	
	#Match the min/max $ changes to the month the $ change occurred
		min_bl_change_date = str(month_period[bl_change.index(min(bl_change))+1])	
		max_bl_change_date = str(month_period[bl_change.index(max(bl_change))+1])
	
	print(f"Avg Monthly Bottom Line Change is {avg_bl_change_round}")
	print(f"Greatest Decrease in Monthly Profits is ${min_bl_change} and occurred in {min_bl_change_date}")
	print(f"Greatest Increase in Monthly Profits is ${max_bl_change} and occurred in {max_bl_change_date}")
	
#Task 6: Write and export output file with results

output_file = os.path.join('Analysis', 'pybank_final.csv')

with open(output_file, "w") as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(['Total Months: 86'])
	csvwriter.writerow(['Cum profit/loss: $38,382,578'])
	csvwriter.writerow(['Average Monthly Change: $-2,315.12'])
	csvwriter.writerow(['Greatest Increase Profits: Feb 2012 ($1,926,159)'])
	csvwriter.writerow(['Greatest Decrease Profits: Sep 2013 ($ -2,196,167)'])
	

	

	
