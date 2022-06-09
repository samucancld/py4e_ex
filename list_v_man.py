tot = 0
c = 0
while True:
    s_num = input('> ')
    if s_num == 'done': break
    f_num = float(s_num)
    tot = tot + f_num
    c = c + 1
avg = tot / c
print(f'Average: {avg}')

my_list = list()
while True:
    val = input('> ')
    if val == 'done': break
    my_list.append(float(val))
print(f'Average: {sum(my_list)/len(my_list)}')