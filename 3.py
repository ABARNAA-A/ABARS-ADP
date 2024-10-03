n=int(input("enter a number:"))
temp=n
r=0
for i in n:
    dig=n%10
    r=dig+r
print(r)
