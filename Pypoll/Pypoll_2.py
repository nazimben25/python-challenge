# import modules

import os
import csv

# Specify the file path to the CSV
path = "F:/github/python-challenge/Resources/election_data.csv"
csvpath = os.path.join(path)

# Open and read the CSV file using UTF-8 encoding
with open(csvpath, mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and print the CSV header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

   # creates 3 empty lists : 'BallotID', 'County', 'Candidate' / this will allow analysis on CANDIDATE list

    ballotID = []
    county = []
    candidatelist = []
    
    # fill the lists by assigning each index to a list
      
    for row in csvreader:
        newID = row[0]
        newcounty = row[1]
        newcandidate = row[2]

        ballotID.append(newID)
        county.append(newcounty)
        candidatelist.append(newcandidate)
        
    
    # calculate TOTAL VOTES = number of entries of any list
    totalvotes = len(ballotID)
    
   
    # calculate results

    ## create new lists candidatedistinct + candidates voters + % to stores the loop result
        
    candidatesdinctinctlist = []    
    candidatesvoterslist = []
    candidatespercentlist = []
        
    ## sort list candidates / the list need to be sorted so we can use the change in value to identify distinct values
    
    candidatelist.sort()

    ## create variables to loop
    
    candidatename = ""
    voters = 0
    
    ## fill the list with distinct values of candidates and their score + %
    
    for value in candidatelist :
        ### if it is the first row then we create 1st candidate, we store it in our list, we update voter number
        if candidatename == "" :  
            candidatename = value
            candidatesdinctinctlist.append(candidatename)
            voters = voters + 1
        
        ### for all other rows
        else : 
            if value != candidatename : 
                #### if it is NOt the first row , AND if the name is different (means new candidate) then we create 1st candidate we store it in our list, we update voter number + store the voters in list
                candidatename = value
                candidatesdinctinctlist.append(candidatename)  ###### update list of candidates with distinct values
                
                voters = voters  ##### calculate the score
                percent = (voters / totalvotes)
                candidatesvoterslist.append(voters) ###### update list of voters count
                candidatespercentlist.append(percent) ###### update list of voters %
                voters = 1 ###### we reset the voters number to be used for the next candidate
            
            ### we just need to update the voter number +1
            else : 
                voters = voters +1
    
    ### the last candidate (last in sorted data) will get it score that still stored in th variables we created
    
    if candidatename :
         candidatesdinctinctlist.append(candidatename)
         candidatesvoterslist.append(voters)
         candidatespercentlist.append(voters/totalvotes)
    
    # find the winner : the greates score in synthesis list
    
    votersmax = max(candidatesvoterslist)
    winner = candidatesdinctinctlist[candidatesvoterslist.index(votersmax)]
    
### these lines can be printed for control/ tracking purpose ONLY
    #print(candidatesdinctinctlist)
    #print(candidatesvoterslist)
    #print(candidatespercentlist)
        
    
    # print all  
    
    ## to show in the terminal
    
    print("                ")
    print("Election Results")
    print("-------------------------")
    print(f"Total votes : {totalvotes}")
    print("-------------------------")

    #extract the resut for each candidate from the lists the values in the same index
    for i in range(len(candidatesdinctinctlist)-1) :
        c = candidatesdinctinctlist[i]
        r = candidatesvoterslist[i]
        p = candidatespercentlist[i]
        formatedp = f"{p:.3%}"
        print(f" {c} {formatedp} ({r})")
    
    
    print("-------------------------")
    print(f"Winner : {winner} ")
    print("-------------------------")
    
    
    
    ## EXPORT to .txt File

    export_path = "F:/github/python-challenge/Pypoll/PollOutput.txt"
    
    with open(export_path, "w") as export :
        
        print("                ", file = export)
        print("Election Results", file = export)
        print("-------------------------", file = export)
        print(f"Total votes : {totalvotes}", file = export)
        print("-------------------------", file = export)

        #extract the resut for each candidate from the lists the values in the same index
        for i in range(len(candidatesdinctinctlist)-1) :
            c = candidatesdinctinctlist[i]
            r = candidatesvoterslist[i]
            p = candidatespercentlist[i]
            formatedp = f"{p:.3%}"
            print(f" {c} {formatedp} ({r})", file = export)
            
        print("-------------------------", file = export)
        print(f"Winner : {winner} ", file = export)
        print("-------------------------", file = export)
