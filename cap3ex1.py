#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours = float(input('Enter Hours> '))
rate = float(input('Enter Rate> '))

if hours > 40:
    ab_hs = hours - 40
    hours = hours - ab_hs
    pay = (hours + (ab_hs * 1.5)) * rate 
else:
    pay = hours * rate

print(pay)


