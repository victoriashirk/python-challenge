import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Create variables
total_votes = 0
cand_votes = {}
cand_percent = {}

# Read CSV file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip the header row
    header = next(csvreader)

    #calc total votes and votes for each candidate
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
    
        if candidate in cand_votes:
            cand_votes[candidate] += 1
        else:
            cand_votes[candidate] = 1

# Calculate the percentages
for candidate in cand_votes:
    cand_percent[candidate] = (cand_votes[candidate] / total_votes) * 100

# Calc the winner
winner = None
max_votes = 0
for candidate in cand_votes:
    if cand_votes[candidate] > max_votes:
        max_votes = cand_votes[candidate]
        winner = candidate

# Print the results
print("Election Results")
print("----------------------")
print("Total Votes: " + str(total_votes))
print("----------------------")
print(cand_percent)
print("----------------------")
print('Winner: ' + winner)
