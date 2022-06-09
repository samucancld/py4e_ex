#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
    try:
        fscore = float(score)
        if fscore < 0.0 or fscore > 1.0:
            raise ValueError
    except:
        return 'bad score'
    if fscore >= 0.9:
        return 'A' 
    elif fscore >= 0.8:
        return 'B' 
    elif fscore >= 0.7:
        return 'C'
    elif fscore >= 0.6:
        return 'D'
    else:
        return 'F'




while True:
    score = input('> ')
    if score == 'done':
        break
    else:
        print(computegrade(score))
