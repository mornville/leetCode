def containsDuplicate(nums):
    nums_set = set(nums)    
    return len(nums) != len(nums_set) 
containsDuplicate([1,3,4,4])
