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

    # Compiles and prints shortened URL
    new_url = begin + body

    if valid0 and valid1:
        print("URL is Valid")
    else:
        print("URL is Invalid")

    print("Shortened URL: " + new_url)
    return new_url

if __name__ == "__main__":
    url = input("Give me a URL: ")
    check_and_shorten_url(url)