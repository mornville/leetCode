def arrayPairSum(nums):
    orderdList = sorted(nums)
    sum = 0
    i=0
    while(i<len(orderdList)-1):
        sum+=min(orderdList[i], orderdList[i+1])
        i+=2

    print(sum)

arrayPairSum([0,0,3,2])