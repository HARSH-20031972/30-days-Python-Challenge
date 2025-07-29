a=[]
for i in range(1):
    x=int(input("Enter Num=")) 
    a.append(x)
if x<100 or x>999:
    print("Invalid Choice")
else:
    num=x
    rev=0
    while num>0:
        d=num%10
        rev=rev*10+d
        num//=10
    if x==rev:
        print("Palindrome")
    else:
        print("Non Palindrome")