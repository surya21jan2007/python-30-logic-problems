#while loop
num=int(input("Enter a nmber:"))
total=0
while 0<num:
    digit=num%10
    total+=digit
    num//=10
print(total)
#for loop
nums=int(input("enter a number:"))
total=0
for digit in nums:
    total+=int(digit)
print(total)

#sum()

num = input("Enter a number: ")
total = sum(int(digit) for digit in num)
print("Sum of digits:", total)
