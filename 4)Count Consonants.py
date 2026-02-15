word=input("Enter a Word:")
vowels='aeiou'
con=0
vow=0
for i in word.lower():
    if i in vowels:
        vow+=1
    elif i.isalpha():
        con+=1
    else:
        pass
print("Vowels:",vow)
print("Consonants:",con)
