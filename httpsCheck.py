url = str(input("Give me a URL: "))
textStart = 0
marker = 0
domain = ""
domainEnd = 0

#Removes the https://
for i in range(0, len(url)):
    if url[i] == "/":
        if url[i+1] == "/":
           if url[i+2] == "w":
               if url[i+3] == "w":
                   if url[i+4] == "w":
                       if url[i+5] == ".":
                            textStart = int(i+5)
        break
shorter = url[textStart + 1:len(url)]

#Finds the domain
for i in range(0, len(shorter)):
    if shorter[i] == ".":
        marker = i
for i in range(marker, len(shorter)):
    if shorter[i] == "/":
        domainEnd = i
j = marker
print(domainEnd)
print(shorter[domainEnd -1])
print(shorter[domainEnd])
i = domainEnd
while j < i:
    domain += shorter[j]
    j += 1
    
print(domain)

#Shortens and adds domain
shorter = shorter[0:marker]
if (len(shorter) <= 10): 
    print("short")
else:
    max = 12 - len(domain)
    shorter = shorter[0:max]
    print(shorter)

shortened = shorter + domain
print(shortened)

