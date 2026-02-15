name=input("Enter a name:")
freq={}
for word in name:
    word=word.lower()
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
for word,count in freq.items():
    print(word,':',count)

'''num=input()
freq={}
for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i,count in freq.items():
    print(i,':',count)

'''
