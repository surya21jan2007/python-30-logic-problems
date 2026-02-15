text=input("Enter a text:")
duplicates={}
for i in text:
    if i!=' ':
        if i in duplicates:
            duplicates[i]+=1
        else:
            duplicates[i]=1
for i,count in duplicates.items():
    print(i,"appers",count,"times")
