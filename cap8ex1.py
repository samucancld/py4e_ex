#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

l1 = [1,2,3,4]
l2 = [5,6,7,8]

def chop(list):
    del list[0]
    list.pop()
    return None

chop(l1)
print(l1)

def middle(list):
    return list[1:len(list)-1]

print(middle(l2))