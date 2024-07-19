import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

#Make variables 
total_months = 0
total_profit = 0
changes = []
prev_profit = None
max_increase = {'date': None, 'amount': 0}
max_decrease = {'date': None, 'amount': 0}

# Read CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip the header row
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        #Calc total number of months
        total_months +=1
        #calc total profit
        total_profit += profit

        #calc max increase and decrease
        if prev_profit is not None:
            change = profit - prev_profit
            changes.append(change)

            if change > greatest_increase['amount']:
                greatest_increase = {'date': date, 'amount': change}
            if change < greatest_decrease['amount']:
                greatest_decrease = {'date': date, 'amount': change}

        prev_profit = profit
        
#calc avg change
average_change = sum(changes) / len(changes)


#Print the results
print("Financial Analysis")
print("-------------------")
print("Total Months: "+ str(total_months) )   
print("Total: "+ "$" + str (total_profit))
print("Average Change: $"+ str(average_change))     
print(f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['amount']})")
print(f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['amount']})")









