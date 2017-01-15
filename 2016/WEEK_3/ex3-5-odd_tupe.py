def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    temp = ()
    for i in range(len(aTup)):
        if not (i % 2):
            temp += (aTup[i],)
    
    return temp
    