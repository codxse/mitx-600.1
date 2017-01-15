def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''    
    temp1 = {}
    temp2 = {}
    for key in list(d1.keys()):
        if key in list(d2.keys()):
            temp1[key] = f(d1[key], d2[key])
            d2.pop(key, None)            
        else:
            temp2[key] = d1[key]
    
    for key, value in d2.items():
        temp2[key] = value
    
    return (temp1, temp2)