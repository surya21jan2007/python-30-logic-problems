name=input("Enter a name:")
vowels='aeiou'
result=''
for i in name:
    if i in vowels:
        result+='*'
    else:
        result+=i

print("Output:",result)
        
