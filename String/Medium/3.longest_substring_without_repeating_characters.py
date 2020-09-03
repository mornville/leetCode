"""
3. Longest Substring Without Repeating Characters
-------------------------------------------------
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum = 0
        substring = ""
        for idx, c in enumerate(s):
            if c in substring:
                substring = substring[substring.find(c)+1:]
            substring += c
            if len(substring) > maximum:
                maximum = len(substring)
        return maximum

"""
Runtime: 32 ms, faster than 98.14% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.1 MB, less than 59.29% of Python online submissions for Longest Substring Without Repeating Characters.
"""