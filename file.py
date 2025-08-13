

##QUANTITY

counts={}

items=["banana","apple","orange","banana","apple","orange","banana","apple","orange",]

for item in items:
    counts[item]=counts.get(item, 0)+1

print(counts)