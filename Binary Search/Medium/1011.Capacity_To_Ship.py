class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        right = sum(weights)
        left = max(weights)
        
        while left < right:
            mid = left + (right-left) // 2
            
            if self.check(weights, mid, D):
                right = mid
            else:
                left = mid+1
        return left
    
    def check(self, weights, mid, D):
        sum = 0        
        days = 1
        
        start, end = 0, len(weights)
        
        while start<end:
            sum+= weights[start]
            if sum>mid:
                sum = weights[start]
                days+=1
                if days > D:
                    return False
            start+=1

        return True
 