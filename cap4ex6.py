#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        ab_hs = hours - 40
        hours = hours - ab_hs
        return (hours + (ab_hs * 1.5)) * rate 
    else:
        return hours * rate



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
    pay = computepay(f_hours,f_rate)
    print(pay)
    break





