print("Sudhanshu Singh")
n=int(input("Enter the no."))
p=n
sum=0
while (p>0):
    r=p%10
    sum += r*r*r
    p=p//10

if sum==n:
    print("Armstrong Number.")
else:
    print("Not an Armstrong Number.") 