import csv

filename = 'URL Database.csv'

header = ['URL']

with open (filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    more = input ('Do you want to add more URLs? (y/n): ')
    if more.lower() == 'y':
        while True:
            url = input ('Enter URL: ')
            writer.writerow([url])
            more = input ('Do you want to add more URLs? (y/n): ')
            if more.lower() != 'y':
                  break
        else:
            print ('No URLs added to database.')

print ('URLs added to database.')