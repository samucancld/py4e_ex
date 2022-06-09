#Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

lon = list()

while True:
    temp = input('> ')
    try:
        ftemp = float(temp)
    except:
        if temp != 'done':
            print("that's not a num")
            continue
        else:
            if len(lon) == 0:
                quit()
            else:
                break
    lon.append(ftemp)

print(lon)
print(f'max: {max(lon)}\nmin: {min(lon)}')
