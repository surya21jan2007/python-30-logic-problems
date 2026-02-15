#For Loop
n=int(input("Enter a how many teams:"))
a,b=0,1
print("Fibonacci Series:")
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
    
#Using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter how many terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")
