"""
451. Sort Characters By Frequency
---------------------------------
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictionary = collections.Counter(s)
        temp = [(char,freq) for char,freq in sorted(dictionary.items(), key=lambda x: (-x[1], x))]
        res = [i*j for i, j in temp]
        return ''.join(res)


"""
Runtime: 52 ms, faster than 77.14% of Python online submissions for Sort Characters By Frequency.
Memory Usage: 15.2 MB, less than 50.36% of Python online submissions for Sort Characters By Frequency.
"""