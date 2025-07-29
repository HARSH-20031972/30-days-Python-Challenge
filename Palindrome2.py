a=[]
for i in range(5):
    while True:
        x=input()
        if len(x)>2:
            a.append(x)
            break
b=[]
for i in a:
    b.append(i[::-1])
print(b)
for i in range(len(b)):
    if a[i]==b[i]:
        print(a[i])
