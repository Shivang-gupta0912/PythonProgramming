# printing Fibonacci sequence upto t term

t = int (input ("Enter the number of terms: "))
t1,t2=0,1
if t==1:
    print(t1)
elif t==2:
    print(t1, t2)
else:
    print(t1,t2,end=" ")
    while t-2>0:
        next=t1+t2
        print(next,end=" ")
        t1=t2
        t2=next
        t=t-1