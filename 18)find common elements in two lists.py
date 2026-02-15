a=[1,2,3]
b=[3,4,5]
common=[]
for items in a:
    if items in b and items not in common:
        common.append(items)

common=list(set(a)&set(b))
print(common)
print(common)

