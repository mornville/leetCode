def reverseInteger(x):
    num = str(x)
    ans = ''
    if(x<10 and x>0):
        print(x)

    for i in range(0, len(num)):
        if(num[i] == '-'):
            flag = 1
        else:
            ans+=num[len(num)-i]
    if(flag == 1):
        ans= '-' + ans
    print(int(ans))
    
reverseInteger(-109)
