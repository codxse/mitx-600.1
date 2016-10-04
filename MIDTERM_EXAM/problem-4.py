def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    if (num == 1):
        return 0
    else:
        product = base
        power = 0
        while (product < num):
            product *= base
            power += 1
    
    if (power == num):
        return power
    else:
        upper_power = base**(power + 1)
        lower_power = base**power
        
        if (abs(num - upper_power) < abs(num - lower_power)):
            return power+1
        return power