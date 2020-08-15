
def isOneBitCharacter(self, bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    i = 0
    while i < len(bits) - 1:
        i += bits[i] + 1
    return i == len(bits) - 1


#second solution
def isOneBitCharacter(self, bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    i = 0
    while(i<=len(bits)-1):
        if(bits[i] == 0):
            i = i+1
            if(i<=len(bits)-1):
                pass
            else:
                return True
        elif(bits[i]==1):
            i = i+2
            if(i<=len(bits)-1):
                pass
            else:
                return False