word=input("Enter a Word:")
vowels="aeiou"
vow=0
for i in word.lower():
    if i in vowels:
        vow+=1
    else:
        pass
print(vow)
