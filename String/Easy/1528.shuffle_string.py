"""
1528. Shuffle String
--------------------
Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

"""
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        temp = [None]*len(s)
        
        for idx, char in enumerate(s):
            temp[indices[idx]] = char
            
        return "".join(temp)
        
"""
Runtime: 40 ms, faster than 87.49% of Python online submissions for Shuffle String.
Memory Usage: 12.7 MB, less than 73.22% of Python online submissions for Shuffle String.
"""