n=int(input("enter a number"))
print(n)

#to check even or odd
if n%2==0:
    print("even")
else:
    print("odd")

#to find the factors
for i in range(1,n+1):
    if n%i==0:
        print(i)