import os
import csv

# Specify the file path to the CSV
path = "F:/github/python-challenge/Resources/budget_data.csv"

csvpath = os.path.join(path)

# Open and read the CSV file using UTF-8 encoding
with open(csvpath, mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and print the CSV header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # creates 3 empty tupples : "'Date', 'Profit/Losses', 'change'

    date_closing = ()
    profit_losses = ()
    change = ()
    
    # fill the tuplles / change = evolution of the result between 2 periods (row)
    previous_result = 0
    
    for row in csvreader:
        newdate = row[0]
        newresult = row[1]
        evolution = float(newresult) - float(previous_result)
        previous_result = newresult # reset the value of previous result to the current row
        
        date_closing = date_closing + (newdate,)
        profit_losses = profit_losses + (float(newresult),)
        change = change + (float(evolution), )
        
    ###print ONLY if you need to controle  
    #print(date_closing)
    #print(profit_losses)
    #print(change)
    
    #total months
    nbmonths = len(date_closing)
    
    # Total result
    totalresult = sum(profit_losses)
    formatedtotalresult = f"${totalresult:.0f}"
    
    # Average change 
    ## create new tupple excluding 1st change value / the first month, we dont calculate an average
    newavg = change[1:]
    avgchange = sum(newavg) / (nbmonths-1)
    formatedavgchange = f"${avgchange:.2f}"
    
    # Greatest Increase in Profits
    increase = max(change)
    formatedincrease = f"${increase:.0f}"
    
    ## find the month : find the index of the great evolution THEN use this index in tupple date_closing
    monthincrease = date_closing[change.index(increase)]
    
    # Greatest Decrease in Profits
    decrease = min(change)
    formateddecrease = f"${decrease:.0f}"
    
    ## find the month : find the index of the great evolution THEN use this index in tupple date_closing
    monthdecrease = date_closing[change.index(decrease)]

    
    # Print all
    
    print("Financial Analysis")
    print("--------------------------------------------------------------------")
    print(f'total months : {nbmonths}')
    print(f'total :  {formatedtotalresult}')
    print(f'Average change  : {formatedavgchange}')
    print(f'Greatest Increase in Profits : {monthincrease} ({formatedincrease})')
    print(f'Greatest Decrease in Profits : {monthdecrease} ({formateddecrease})')    
    
    # EXPORT

    export_path = "F:/github/python-challenge/Pybank/bankOutput.txt"
    
    with open(export_path, "w") as export :
        
        print("Financial Analysis", file = export)
        print("--------------------------------------------------------------------", file = export)
        print(f'total months : {nbmonths}', file = export)
        print(f'total :  {formatedtotalresult}', file = export)
        print(f'Average change  : {formatedavgchange}', file = export)
        print(f'Greatest Increase in Profits : {monthincrease} ({formatedincrease})', file = export)
        print(f'Greatest Decrease in Profits : {monthdecrease} ({formateddecrease})', file = export)    