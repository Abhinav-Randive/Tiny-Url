import csv
# from short_url_module import generate_short_url  # Import the function from the other module

filename = 'URL Database.csv'

header = ['Number', 'URL', 'Short URL']

with open(filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)

    more = input('Do you want to add more URLs? (y/n): ')
    if more.lower() == 'y':
        count = 1
        while True:
            url = input('Enter URL: ')
            # short_url = generate_short_url(url)  # Generate the short URL using the imported function

            writer.writerow([count, url]) #short_url to be added later
            count += 1
            more = input('Do you want to add more URLs? (y/n): ')
            if more.lower() != 'y':
                break
    else:
        print('No URLs added to database.')

print('URLs added to database.')