

while True:
    score = input('> ')
    if score == 'done':
        break
    try:
        fscore = float(score)
    except:
        print('bad score')
        continue
    if fscore >= 0.9 and fscore <= 1.0:
        print('A')
    elif fscore >= 0.8 and fscore <= 1.0:
        print('B')
    elif fscore >= 0.7 and fscore <= 1.0:
        print('C')
    elif fscore >= 0.6 and fscore <= 1.0:
        print('D')
    elif fscore < 0.6 and fscore <= 1.0:
        print('F')
    else:
        print('bad score')
        continue
