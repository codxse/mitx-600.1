def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if (len(aStr) > 1):
        mid_char = aStr[len(aStr) // 2]
        mid_index = len(aStr) //  2
        
        if(char == mid_char):
            return True
            
        if(char > mid_char):
            aStr = aStr[mid_index:]
            return isIn(char, aStr)
            
        if(char < mid_char):
            aStr = aStr[0:mid_index]
            if(len(aStr) == 2):
                return char == aStr[0] or char == aStr[1]
            return isIn(char, aStr)
    
    return False