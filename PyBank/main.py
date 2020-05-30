import os
import csv

# Define input csv file
budget_csv = os.path.join("Resources", "budget_data.csv")
# months_total = 0
net_total = 0

# Lists to hold months, profit/loss numbers and profit/loss changes
Profit_loss_months =[]
Profit_loss_numbers =[]
holder=[]

# Open and read the CSV file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first of budget_data.csv
    csv_header = next(csvfile)

    # row = list(csvreader)

    # Read through each row of data after the header
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        # Add 1 to Total Months counter
        # months_total +=1

        # Add monthy profit_loss to net total
        net_total = (net_total + profit_loss)
    
        # add each month to a list
        Profit_loss_months.append(date)
        
        # add each profit_loss amount to a list
        Profit_loss_numbers.append(profit_loss)

# Find the average change
for i in range(1, len(Profit_loss_numbers)):    
    pc = Profit_loss_numbers[i]-int(Profit_loss_numbers[i-1])
    holder.append(pc)
    # print(f"Number: {i} || {pc}")

avg_changes = sum(holder) / len(holder) 
# Format the average change value
avg_changes = round(avg_changes,2)

# Find the greatest increase and decrease in profits
max_increase = max(holder)
max_decrease = min(holder)

# Use the greatest increase and decrease in profits to get the date of that increase and decrease
# NOTE: have to use +1 because the actual increase or decrease happens in the following month by my calculation  
max_increase_month_index = holder.index(max_increase)+1
max_increase_month = Profit_loss_months[max_increase_month_index]
max_decrease_month_index = holder.index(max_decrease)+1
max_decrease_month = Profit_loss_months[max_decrease_month_index]

# Print Analysis to terminal
print(" ")
print("Financial Analysis")
print("---------------------------------")
# print(f"Total Months: {int(months_total)}" )
print(f"Total Months: {len(Profit_loss_months)}" )
print(f"Total: ${int(net_total)}" )
print(f"Average Change: ${avg_changes}")
print(f"Greatest Increase in Profits: {max_increase_month} ${max_increase}")
print(f"Greatest Decrease in Profits: {max_decrease_month} ${max_decrease}")

# Print Analysis to file
file = open("financial_analysis.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("---------------------------------" + "\n")
file.write(f"Total Months: {len(Profit_loss_months)}" + "\n")
file.write(f"Total: ${int(net_total)}" + "\n")
file.write(f"Average Change: ${avg_changes}" + "\n")
file.write(f"Greatest Increase in Profits: {max_increase_month} ${max_increase}" + "\n")
file.write(f"Greatest Decrease in Profits: {max_decrease_month} ${max_decrease}" + "\n")
file.close