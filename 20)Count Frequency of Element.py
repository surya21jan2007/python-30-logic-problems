num=input("Enter a number:")
freq={}
for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i,count in freq.items():
    print(i,':',count)
