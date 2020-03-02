def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """

    total = 0 
    ans = 0
    temp = 0
    if(int(num/10) == 0):
        return num
    while(num>0):
        total = total + num%10
        temp = total
        if(int(total/10)!=0):
            while(temp>0):
                ans = ans + temp%10 
                temp/=10
    
        num /= 10
    
    return(ans)

addDigits(129)