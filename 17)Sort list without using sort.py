num=[78,98,100,21,76]

for i in range(len(num)):
    for j in range(0,len(num)-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)
