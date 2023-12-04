i=1
res=0
while i<11 :
    for r in range(1, 11):
        res=r*i
        if res<10:
            print(res,end="  ")
        else:
             print(res,end=" ")
    i+=1
    print()
