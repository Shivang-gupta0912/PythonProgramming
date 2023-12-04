# printing all prime numbers in an interval

# taking limits of interval
lower=int(input("Enter lower limit of interval: "))
upper=int(input("Enter upper limit of interval: "))

if lower>upper:
    print("Please input correct interval")
else:
    for num in range(lower, upper+1):
        for i in range (2, num):
            if num%i==0:
                break
        else:
            print(num, end=" ")