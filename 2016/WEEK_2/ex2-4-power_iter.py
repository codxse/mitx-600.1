def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    base_powered_by_exp = 1
    for i in range(exp):
       base_powered_by_exp *= base
       
    return base_powered_by_exp