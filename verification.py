# Make sure there are no duplications in the long URL
import csv
import os

def noDuplication(fileName, newURL):
    #print("noDup called")

    with open(fileName, 'r') as file:
        # creating a csv reader object
        csvreader = csv.reader(file)
        
        #only reads the first row in csvreader???        
        for row in csvreader: 
            if row[1] == newURL:
                return True
    
    return False