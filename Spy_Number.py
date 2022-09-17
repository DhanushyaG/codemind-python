n=int(input())
s1=1
s2=0
while n>0:
    r=n%10
    s1*=r
    s2+=r
    n=n//10
if s1==s2:
    print("Spy Number")
else:
    print("Not Spy Number")