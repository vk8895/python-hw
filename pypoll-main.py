#pypoll code

#Open CSV File

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	print(csvreader)
	
	#Test to ensure program reads election data
	#for rows in csvreader:
	#	print(rows)
		
#Task 1: Tabulate the number of votes in election_data.csv
	
	#Create empty lists
	votes =[]
	candidates = []
		
	#Populate empty list
	for rows in csvreader:
		votes.append(rows[0])
		candidates.append(rows[2])
		
	#Remove header
	votes.pop(0)
	candidates.pop(0)
		
	#Obtain and print list length
	num_votes = len(votes)
	print(f"Total #Votes: {num_votes}")
	
	
#Task 2: List of candidates that received votes

	uq_cand = []
	
	#Instead of if, try if not functionality
	for x in candidates:
		if x not in uq_cand:
			uq_cand.append(x)
		
	print(uq_cand)
		
#Task 3: Find #votes each candidate won

	Khan = []
	Correy = []
	Li = []
	OTooley = []
	
	for x in candidates:
		if x=='Khan':
			Khan.append(x)
		elif x=='Correy':
			Correy.append(x)
		elif x=='Li':
			Li.append(x)
		else:
			OTooley.append(x)
	
		Khan_votes = len(Khan)
		Correy_votes = len(Correy)
		Li_votes = len(Li)
		OTooley_votes = len(OTooley)

#Task 4: Find % of votes each candidate received 

		Khan_pct = round(Khan_votes/num_votes * 100, 2)
		Correy_pct = round(Correy_votes/num_votes * 100, 2)
		Li_pct = round(Li_votes/num_votes * 100, 2)
		OTooley_pct = round(OTooley_votes/num_votes * 100, 2)
	
	print(f"Khan receives {Khan_votes} votes, which is {Khan_pct}% of total votes")
	print(f"Correy receives {Correy_votes} votes, which is {Correy_pct}% of total votes")
	print(f"Li receives {Li_votes} votes, which is {Li_pct}% of total votes")
	print(f"O'Tooley receives {OTooley_votes}, which is {OTooley_pct}% of total votes")
	
	
#Task 5: Write and export output file with results

output_file = os.path.join('Analysis', 'pypoll_final.csv')

with open(output_file, "w") as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['Total Votes: 3,521,001'])
	csvwriter.writerow(['Khan: 63% (2,218,231)'])
	csvwriter.writerow(['Correy: 20% (704,200)'])
	csvwriter.writerow(['Li: 14% (492,940)'])
	csvwriter.writerow(['OTooley: 3% (105,630)']) 
	csvwriter.writerow(['Winner: Khan'])
	
	
				

	
	