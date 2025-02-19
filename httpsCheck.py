url = str(input("Give me a URL: "))
textStart = 0
marker = 0
domain = ""
domainEnd = 0

#Removes the https://
for i in range(0, len(url)):
    if url[i] == "/":
        if url[i+1] == "/":
            textStart = int(i+1)
        break
shorter = url[textStart + 1:len(url)]
print(shorter)

if shorter[0] == "w":
    if shorter[1] == "w":
        if shorter[2] == "w":
            if shorter[3] == ".":
                shorter = shorter[4:len(shorter)]
print(shorter)
#Finds the domain
for i in range(0, len(shorter)):
    if shorter[i] == ".":
        marker = i
for i in range(marker, len(shorter)):
    if shorter[i] == "/":
        domainEnd = i
        break
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

