import csv
from httpsCheck import check_and_shorten_url  # Import the function from the other module
from verification import noDuplication

filename = 'URL Database.csv'

header = ['Number', 'URL', 'Short URL']

with open(filename, 'w') as file:
    with open(filename, 'a', newline = '') as file:
        readWriter = csv.writer(file)
        readWriter.writerow(header)
    more = input('Do you want to add more URLs? (y/n): ')
    if more.lower() == 'y':
        count = 1
        while True:
            url = input('Enter URL: ')
            short_url = check_and_shorten_url(url)  # Generate the short URL using the function

            with open(filename, 'a', newline = '') as file:
                readWriter = csv.writer(file)

                # Make sure the same long URL is not added twice
                if not noDuplication(filename, url):
                    readWriter.writerow([count, url, short_url])  # Write the URL and short URL to the CSV file
                    count += 1
                    print("Adding the URL.")
                else:
                    print("This URL has already been added.")            
            
            more = input('Do you want to add more URLs? (y/n): ')
            if more.lower() != 'y':
                break
    else:
        print('No URLs added to database.')
        
    print('URLs added to database.')