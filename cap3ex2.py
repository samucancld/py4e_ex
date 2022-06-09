#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input


while True:
    #s_hours = input('Enter Hours> ')
    #s_rate = input('Enter Rate> ')
    try:
        #f_hours = float(s_hours)
        #f_rate = float(s_rate)
        f_hours = float(input('Enter Hours> '))
        while True:
            try:
                f_rate = float(input('Enter Rate> '))
                break
            except: 
                print('Error, please enter numeric input')
                continue
    except:
        print('Error, please enter numeric input')
        continue
    if f_hours > 40:
        ab_hs = f_hours - 40
        f_hours = f_hours - ab_hs
        pay = (f_hours + (ab_hs * 1.5)) * f_rate 
    else:
        pay = f_hours * f_rate
    print(pay)
    break


