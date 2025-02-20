url = str(input("Give me a URL: "))
marker = 0
begin = ""

#Removes the https://
if url.startswith("https://"):
    url = url[8:]
    begin = "https://"
elif url.startswith("http://"):
    url = url[7:]
    begin = "http://"
print(url)
#Removes the www. if it exists
if url.startswith("www."):
    url = url[4:]
print(url)

#Finds the main body of the url discluding all after "/""
for i in range(len(url)):
    if url[i] == "/":
        marker = i
        break
print(marker)
body = url[0:marker + 5]

#compiles and prints shortened url
newUrl = begin + body
print(newUrl)

