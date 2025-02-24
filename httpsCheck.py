url = str(input("Give me a URL: "))
marker = 0
begin = ""
valid0 = False
valid1 = False
#Removes the https://
if url.startswith("https://"):
    url = url[8:]
    begin = "https://"
    valid0 = True
elif url.startswith("http://"):
    url = url[7:]
    begin = "http://"
    valid0 = True

#Removes the www. if it exists
if url.startswith("www."):
    url = url[4:]

#Finds the main body of the url discluding all after "/""
for i in range(len(url)):
    if url[i] == "/":
        marker = i
        break
body = url[0:marker + 5]

for i in range (len(body)):
    if body[i] == ".":
        valid1 = True
        break

#compiles and prints shortened url
newUrl = begin + body


if(valid0 == True and valid1 == True):
    print("URL is Valid")
else:
    print("URL is Invalid")
print("Shortened URL: " + newUrl)