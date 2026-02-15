def largest_word():
    sentence=input("Enter a Sentence:")
    words=sentence.split()
    largest=max(words,key=len)
    print(largest)
largest_word()

def largest_word(sentence):
    word=sentence.split()
    largest=""
    for words in word:
        if len(word)>len(largest):
            largest=word
    return largest
sentence="i love programming in python language"
print(largest_word(sentence))
