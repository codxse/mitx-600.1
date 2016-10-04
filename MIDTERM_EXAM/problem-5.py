def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    new_list = list(map(lambda x,y: x*y, listA,listB))
    total = 0
    for number in new_list:
        total += number
    return total