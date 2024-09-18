# import modules

import os
import csv

# Specify the file path to the CSV 
path = "../Resources/budget_data.csv"

csvpath = os.path.join("..","Resources","budget_data.csv")

# Open and read the CSV file using UTF-8 encoding
with open(csvpath, mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and print the CSV header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # creates 3 empty tupples : "'Date', 'Profit/Losses', 'change' / these tupples will be used to process the data

    date_closing = ()
    profit_losses = ()
    change = ()
    
    ## fill the tuplles / for CHANGE = evolution of the result between 2 periods (2 rows)
    previous_result = 0
    
    for row in csvreader:
        newdate = row[0]
        newresult = row[1]
        evolution = float(newresult) - float(previous_result)
        previous_result = newresult # reset the value of previous result to the current row
        
        date_closing = date_closing + (newdate,)
        profit_losses = profit_losses + (float(newresult),)
        change = change + (float(evolution), )
        
###print ONLY if you need to control or track  
    #print(date_closing)
    #print(profit_losses)
    #print(change)
    
    # calculate TOTAL MONTHS
    
    nbmonths = len(date_closing)
    
    # calculate TOTAL RESULT
    
    totalresult = sum(profit_losses)
    formatedtotalresult = f"${totalresult:.0f}" ## to format the number 
    
    # calculate Average change 
    
    ## create new tupple excluding 1st change value / because the first month, we don't calculate a variation
    
    newavg = change[1:]
    
    avgchange = sum(newavg) / (nbmonths-1) ## calculate the average on the tupple
    formatedavgchange = f"${avgchange:.2f}" ## to format the number 
    
    # Greatest Increase in Profits on CHANGE
    
    increase = max(change)
    formatedincrease = f"${increase:.0f}" ## to format the number 
    
    ## find the month : find the index of the greatest evolution in tupple CHANGE THEN use this index in tupple date_closing
    
    monthincrease = date_closing[change.index(increase)]
    
    # Greatest Decrease in Profits on CHANGE
    decrease = min(change)
    formateddecrease = f"${decrease:.0f}" ## to format the number 
    
    ## find the month : find the index of the greatest evolution in tupple CHANGE THEN use this index in tupple date_closing
    monthdecrease = date_closing[change.index(decrease)]

    
    # Print all
    
    ## for terminal purpose
    
    print("Financial Analysis")
    print("--------------------------------------------------------------------")
    print(f'Total months : {nbmonths}')
    print(f'Total :  {formatedtotalresult}')
    print(f'Average change  : {formatedavgchange}')
    print(f'Greatest Increase in Profits : {monthincrease} ({formatedincrease})')
    print(f'Greatest Decrease in Profits : {monthdecrease} ({formateddecrease})')    
    
    ## to be exported to .txt file

    export_path = "../analysis/BankOutput.txt"
    
    with open(export_path, "w") as export :
        
        print("Financial Analysis", file = export)
        print("--------------------------------------------------------------------", file = export)
        print(f'Total months : {nbmonths}', file = export)
        print(f'Total :  {formatedtotalresult}', file = export)
        print(f'Average change  : {formatedavgchange}', file = export)
        print(f'Greatest Increase in Profits : {monthincrease} ({formatedincrease})', file = export)
        print(f'Greatest Decrease in Profits : {monthdecrease} ({formateddecrease})', file = export)    