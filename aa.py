
##1
region=[]
with open("data.txt","r") as d:
    next(d)
    for line in d:
        row=line.rstrip().split(",")
        if row[4] == "Oman":
            region.append(int(row[6]))
##print(region)
aft=[]
for row in region:
    if row <= 1971:
        aft.append(row)
print(aft)

##2
region=[]
with open("data.txt","r") as d:
    next(d)
    for line in d:
        row=line.rstrip().split(",")
        if row[4] == "Latvia":
            region.append(int(row[8]))

print(sum(region))

##3
region=[]
with open("data.txt","r") as d:
    next(d)
    for line in d:
        row=line.rstrip().split(",")
        if row[4] == "Latvia" and row[7] == "Telecommunications":
            region.append(int(row[8]))

print(sum(region))

##4
region=[]
with open("data.txt","r") as d:
    next(d)
    for line in d:
        row=line.rstrip().split(",")
        if row[4] == "Latvia":
            region.append(row[3])

count=0
for row in region:
    row=row.rstrip().split("/")
##    print(row)
    if row[0] == "https:":
        count = count + 1

print(count)

##5
region=[]
with open("data.txt","r") as d:
    next(d)
    for line in d:
        row=line.rstrip().split(",")
        if row[4] == "Latvia":
            region.append(row[3])

count=0
for row in region:
    row=row.rstrip().split(".")
##    print(row)
    if row[1] == "org/":
        count = count + 1

print(count)