'''
for century year which is divisible by 100:
check divisibility by 400
if it is divisible then it is a leap year

for normal year which is not divisible by 100:
check divisibility by 4
if it is divisible then it is a leap year
'''

year= int (input("Enter the Year: "))
if year%100==0 and year%400==0:
    print("Leap Year")
elif year%100!=0 and year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")