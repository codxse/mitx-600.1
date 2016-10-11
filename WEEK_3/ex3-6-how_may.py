def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    t = 0
    for vals in aDict.values():
        t += len(vals)
    
    return t