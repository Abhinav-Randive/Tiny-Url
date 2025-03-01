import csv

def check_and_shorten_url(url):
    marker = 0
    begin = ""
    valid0 = False
    valid1 = False

    # Removes the https:// or http://
    if url.startswith("https://"):
        url = url[8:]
        begin = "https://"
        valid0 = True
    elif url.startswith("http://"):
        url = url[7:]
        begin = "http://"
        valid0 = True

    # Removes the www. if it exists
    if url.startswith("www."):
        url = url[4:]

    # Finds the main body of the URL excluding all after "/"
    for i in range(len(url)):
        if url[i] == "/":
            marker = i
            break
    else:
        marker = len(url)

    body = url[:marker]

    for i in range(len(body)):
        if body[i] == ".":
            valid1 = True
            break
    # Slightly adjust shortened url
    new_url = begin + body

    files = []
    with open("URL Database.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 3:
                files.append(row)
    files = files[1:]
    duplicate = []
    for i in range(len(files)):
        if new_url == files[i][2]:
                duplicate.append(i)
                new_url = new_url + "/" + str(i)
                i = 0

    # Compiles and prints shortened URL

    if valid0 and valid1:
        print("URL is Valid")
    else:
        print("URL is Invalid")

    print("Shortened URL: " + new_url)
    return new_url


if __name__ == "__main__":
    url = input("Give me a URL: ")
    check_and_shorten_url(url)