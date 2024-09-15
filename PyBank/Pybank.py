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
    


    ## calculate number Months + Total results
    
    NbRow = 0
    Total = 0
    previous_result = 0
    change = []
    
    for row in csvreader:
        NbRow = NbRow +1
        Total = Total + float(row[1])
        
        #change ; we calculate the change in the result between previous and current and store it in a list named CHANGE
        change.append(float(row[1])-previous_result)
        
        #we also add a new index to row
        row.append(float(row[1])-previous_result)
        
        # we reset the previous result as the current one
        previous_result = float(row[1]) 
    
    for row in csvreader :
        print(row)
     
    #avg_change = avg_change/NbRow
    change.pop(0)   #remove 1st value from the list equal to the first month without a change
    average_change  = sum(change)/(NbRow-1)  #calculated without the 1st month
    
    change.insert(0,0)   #insert a change value in 1st month equal to 0
    
                                    
    ## greatest increase and decrease
    great_increase_1 = max(change)
    great_decrease_1 = min(change)
    
    # find the month
    month = "glouglou"
    great_increase_test = 0
    for row in csvreader:
        if float(row[1]) > great_increase_test :
            great_increase_test = float(row[1])
            month = row[0] 

    

    
    # summary
    print(f"Total Months : {NbRow}")
    print(f"Total result : {Total}")
    print(f"average change : {average_change}")
    print(f"great_increase in profits  {great_increase_1}")
    print(f"great_decrease in profits  {great_decrease_1}")
    print(f"test  {great_increase_test}")   
    print(month)
