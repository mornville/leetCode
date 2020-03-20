import time
start_time = time.time()
print(start_time)
def threeSum(nums):
    ans = []
    n = len(nums)
    for i in range(n - 1):  
        s = set() 
        for j in range(i + 1, n): 
            x = -(nums[i] + nums[j]) 
            if x in s: 
                if(nums[i+1] + nums[i] + nums[j]==0):
                    if([nums[i], nums[i+1], nums[j]] in ans or [nums[i], nums[j], nums[i+1]] in ans or [nums[i+1], nums[i], nums[j]] in ans or [nums[i+1], nums[j], nums[i]] in ans or [nums[j], nums[i+1], nums[i]] in ans or [nums[j], nums[i], nums[i+1]] in ans):
                        pass
                    else:
                        ans.append([x, nums[i], nums[j]]) 
            else: 
                s.add(nums[j]) 

    for x in s:
        print(x)

threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])            
print("--- %s seconds ---" % (time.time() - start_time))
