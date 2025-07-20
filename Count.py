def parameter(*t):
    odd=even=0
    for i in t:
        if i%2!=0:
            odd+=1
        else:
            even+=1
    print(odd,even)
parameter(1,2,3,4,5,6,7,8,9,10)