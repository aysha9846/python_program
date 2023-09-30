year=int(input("enter the year to check leap year or not :"))
if year%4==0|(year%400 and year%100!=0):
    print(year,"is leap year")
else:
    print(year,"not a leap year")
