def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    min_ = min(a, b)
    max_ = max(a, b)
    
    if(max_ % min_ == 0):
        return min_
    else:
        gcd = min_ - 1
        while(gcd):
            if(min_ % gcd == 0 and max_ % gcd == 0):
                return gcd
            gcd -= 1

