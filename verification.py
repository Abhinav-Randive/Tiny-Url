# Make sure there are no duplications in the long URL
import csv
import os

def noDuplication(fileName, newURL):
    #print("noDup called")
    with open(fileName, 'r') as file:
        # creating a csv reader object
        csvreader = csv.reader(file)

        #if os.stat(fileName).st_size != 0:

        #only reads the first row in csvreader???        
        for row in csvreader: 
            print("testing in function",row)
            #print(newURL)
            if row[1] == newURL:
                    print(row[1])
                    print("The file exists")
                    return True
            else:
                print("The file does not exist; can be added")
                return False
        # always reads the file as empty
        #elif os.stat(fileName).st_size == 0:
        #    print("Empty")
        #    return False
        #else:
        #    print("Something else went wrong")

#noDuplication("URL Database.csv", "https://moodle-2425.wooster.edu/mod/assign/view.php?id=52597")
    #except FileNotFoundError:
    #    print("File not found")
    
        #except pandas.errors.EmptyDataError:
        #    print("The CSV file is empty.")
        #    return False

# Make shortened URLs distinct
