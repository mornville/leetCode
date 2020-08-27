"""
387. First Unique Character in a String
---------------------------------------
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 
Note: You may assume the string contains only lowercase English letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1

"""
-> Runtime: 228 ms, faster than 45.80% of Python online submissions for First Unique Character in a String.
-> Memory Usage: 13 MB, less than 95.65% of Python online submissions for First Unique Character in a String.
"""