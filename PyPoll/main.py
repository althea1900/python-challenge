import os
import csv

# Define input csv file
election_csv = os.path.join("Resources", "election_test.csv")

# Lists to hold votes, candidates
votes =[]
candidates =[]

# Open and read the CSV file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first of budget_data.csv
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:

        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # add each month to a list
        votes.append(voter_id)
        
        total_votes = len(votes)

# Print Analysis to terminal
print(" ")
print("Election Results")
print("---------------------------------")
print(f"Total Votess: {total_votes}" )
print("---------------------------------")