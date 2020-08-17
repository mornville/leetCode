class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 0
        output = [None]*len(nums)
        if len(nums) == 0:
            return nums
        
        prevProd = 1
        prod = 1
        while p1<len(nums):
            prod = 1
            p2 = p1+1
            while p2<len(nums):
                prod = prod * nums[p2]
                p2+=1
            output[p1] = prod * prevProd
            prevProd = prevProd*nums[p1]
            p1+=1
        return output