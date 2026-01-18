print("Sudhanshu Singh")
n=int(input("Enter the no."))
p=n
sum=0
while (n>0):
    r=n%10
    n=n//10
    sum = sum*10+r
if(sum==p):
    print("No. is Palindrome")
else:
    print("No. is Not a Palindrome")
