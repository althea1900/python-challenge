import os
import csv

# define input csv file
budget_csv = os.path.join("Resources", "budget_data.csv")
months_total = 0
net_total = 0
profit_loss = 0

# open and read the CSV file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first of budget_data..csv
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        # print(f'{str(date)} + {int(profit_loss)}')

        # Add 1 to Total Months counter
        months_total +=1
        net_total = (net_total + profit_loss)
    

print(" ")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {int(months_total)}" )
print(f"Total: ${int(net_total)}" )