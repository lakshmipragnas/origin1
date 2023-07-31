n=int(input("enter a number"))
print(n)

#to find factorial
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

#to print multiplication table
for i in range(1,11):
    print(n,"*",i,"=",n*i)