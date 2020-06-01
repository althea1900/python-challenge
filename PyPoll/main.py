import os
import csv

# Define input csv file
election_csv = os.path.join("Resources", "election_data.csv")

# Lists to hold votes, candidates
votes =[]
candidates_list=[]

#Dictionary to hold canidates and votes recieved
candidates_votes = dict()

#Increment value
i = 1

#store winner
highest_votes = 0
winner = ""

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

        # make a list of unique candidates
        if candidate in candidates_list:
            # print("canidate in list, add to count")
            # print(len(candidates_votes))
            for x in range(1, len(candidates_list)+1): 
                if (candidates_votes[x]['name']) == candidate:
                    # print("got it, now add to vote")
                    candidates_votes[x]['votes'] +=1
        else:
            # print("add to list")
            candidates_list.append(candidate)
            candidates_votes[i] = {"name": candidate, "votes": 1,}
            i+=1
   
    # print(candidates_list)
    # print(candidates_votes)
    # print(len(candidates_votes))
     
    total_votes = len(votes)
 

# Print Analysis to terminal
print(" ")
print("Election Results")
print("---------------------------------")
print(f"Total Votess: {total_votes}" )
print("---------------------------------")
for x in range(1, len(candidates_votes)+1): 
    vote_percentage = (candidates_votes[x]['votes'])/total_votes * 100
    # Format the vote_percentage value
    percentage = round(vote_percentage,2)
    print(f"{(candidates_votes[x]['name'])}: {percentage}% ({(candidates_votes[x]['votes'])})")
    # find largest number of votes
    if (candidates_votes[x]['votes']) > highest_votes:
        winner = (candidates_votes[x]['name'])
        highest_votes = (candidates_votes[x]['votes'])
print("---------------------------------")
print(f"Winner: {winner}")
print("---------------------------------")

# Print Analysis to file
file = open("polling_analysis.txt", "w")
file.write("Election Results" + "\n")
file.write("---------------------------------" + "\n")
file.write(f"Total Votess: {total_votes}" + "\n")
file.write("---------------------------------" + "\n")
for x in range(1, len(candidates_votes)+1): 
    vote_percentage = (candidates_votes[x]['votes'])/total_votes * 100
    # Format the vote_percentage value
    percentage = round(vote_percentage,2)
    file.write(f"{(candidates_votes[x]['name'])}: {percentage}% ({(candidates_votes[x]['votes'])})" + "\n")
    # find largest number of votes
    if (candidates_votes[x]['votes']) > highest_votes:
        winner = (candidates_votes[x]['name'])
        highest_votes = (candidates_votes[x]['votes'])
file.write("---------------------------------" + "\n")
file.write(f"Winner: {winner}" + "\n")
file.write("---------------------------------" + "\n")