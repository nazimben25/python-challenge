import os
import csv

# Specify the file path to the CSV
path = "F:/github/python-challenge/Resources/election_data.csv"
csvpath = os.path.join(path)


# distinct candidates
set_candidates = set()


# Open and read the CSV file using UTF-8 encoding
with open(csvpath, mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and print the CSV header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #number of voters
    nb = 0
    for row in csvreader :
        nb = nb+1
    print(f'Total votes = {nb}')


    
    for row in csvreader :
        if len(row) >2 : 
            set_candidates.add(row[2])
        else : 
            print("pas 2 colonnes")
        
    for candidate in set_candidates:
        print(candidate)

    
    
    
    
    
