num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10   # remove last digit

print("Number of digits:", count)
