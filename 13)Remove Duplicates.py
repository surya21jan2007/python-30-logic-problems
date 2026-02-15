num=list(map(int,input().split()))
seen=set()
duplicates=[]
for items in num:
    if items in seen and items not in duplicates:
        duplicates.append(items)
    else:
        seen.add(items)
print(duplicates)
