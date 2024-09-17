# python-challenge
Output for challenge module 3( Python start) - UoT

1)  repository content 
in the repository there are 

- 02 csv files with the data 

- 02 folders for each analysis : PyBank, PyPoll
    in each folder there is the .py file

- 01 folder "analysis that contains 2 txt files with the output of the codes
    - the .txt files filled by the code

2) code structure

2.1) commun structure for both codes

    2.1.1) Open and read the csv
    - use of WITH and OPEN functions
    - use of method "UTF-8" to read the files
    - delimiter ","
    - Assign same file name : csvreader
    - source files are in the same folder F:/github/python-challenge/Resources/ represnted as ../resources/file.csv

    2.1.2) extract the header
    use of "NEXT" function to extract 1st row and use it as header

    2.1.3) Export to .txt
    - use of WITH and OPEN functions
    - duplicate the printed values for the terminal + txt file creation / modification
    - the txt files are located in each folder respectively

    2.1.4) creation of lists and tupples
    the data is stocked in lists and topples, so we can analyse it easily 
    - tupple for PyBank : the data is limited and we needed to keep it unchanged 
    - list for PyPoll : the data is larger (tupple was ineffiscient) and we dont mind if it changes : we needed to sort it once

    2.1.5) I imported and used 2 modules : OS and CSV


2.2) structure for PyBank.py
- creation of 3 tupples : 'Date', 'Profit/Losses', 'change' filled  with forloop
    - calculate the change by difference between the result of the periode and the result of the previous period
- calculation of the requested values using max, min, sum functions on the tupples
- retrieve the months of max and min change by their position in the tupples


2.3) structure for PyPoll.py
- creation of 3 lists : 'BallotID', 'County', 'Candidate'  , filled with with forloop
    - calculation of voters number 

    - creation synthesis list by creating 3 SETS to get the distinct values of candidates with their score : candidate name , candidate score, and %
    - sorting the list (candidate) to allow the calculation of score
    - for each candidate, the score is calculated by looping 
        - search for  the change of the candidate value (hense the sorting)
    - the % is calculated by dividing by the total voters

- find the winner : higher value of synthesis list