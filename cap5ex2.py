#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

min = None
max = None
my_list = []

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    my_list.append(fval)

    if min is None or fval < min:
        min = fval
    if max is None or fval > max:
        max = fval

#print('ALL DONE')
print(max,min)