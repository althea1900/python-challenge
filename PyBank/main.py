import os
import csv

# define input csv file
budget_csv = os.path.join("Resources", "budget_data.csv")
months_total = 0
net_total = 0
profit_loss = 0
next_profit_loss = 0
change = 0
avg_change = 0
Profit_loss_numbers =[]
Profit_loss_changes =[]
holder=[]

# open and read the CSV file
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first of budget_data..csv
    csv_header = next(csvfile)

    # Read through each row of data after the header
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        # Add 1 to Total Months counter
        months_total +=1

        # Add monthy profit_loss to net total
        net_total = (net_total + profit_loss)
    
        # subtract each months proit_loss from the last
        # change = (profit_loss - next_profit_lost)

        # add each profit_loss amount to a list
        Profit_loss_numbers.append(profit_loss)

# calculate avg change in profit_loss

# def average_change(startVal, currentVal):
#    return ((float(currentVal)-startVal)/abs(startVal)) 
# for eachN in Profit_loss_numbers:
#     pc = average_change(Profit_loss_numbers[0], eachN)
#     print(f"Number: {eachN} || {pc}")
# # print(f"Number: {eachN} || {pc}") 
# avg_change = pc
# # print(pc)          


for i in range(len(Profit_loss_numbers)-1):
    pc = Profit_loss_numbers[i+1]-Profit_loss_numbers[i]
    holder.append(pc)
    print(f"Number: {i} || {pc}")
    # print(eachN)(pc) 
    change = sum(holder) / len(holder) 
# print(f"Number: {change}")
avg_changes = pc
# print(pc)

# print(f"range: {range(len(Profit_loss_numbers))}")
# print(f"len: {len(Profit_loss_numbers)}")
# print(f"len of holer: {len(holder)}")
# Print Analysis to terminal
print(" ")
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {int(months_total)}" )
print(f"Total: ${int(net_total)}" )
print(f"Average Change: ${round(change,2)}")