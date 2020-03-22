def uniqueOccurrences(arr):
    temp = []
    count = 0
    j=0
    arr = sorted(arr)
    i = 0
    while(i<len(arr)-1):
        if(arr[i] == arr[i+1]):
            count+=1
            i+=1
        else:
            if(count not in temp):
                temp.append(count)
            elif(count in temp):
                print('false')
            elif(count == 0):
                temp.append(count)
            count = 0
            i+=1
    if(arr[i] == arr[i-1]):
        count+=1
        if(count not in temp):
            temp.append(count)
        elif(count in temp):
            print('False2')
        elif(count == 0):
            temp.append(count)
    else:
        if(count in temp):
            print('finalFalse')
        
    print('true')        

uniqueOccurrences([1,1,2,2])
            
