"""
165. Compare Version Numbers
----------------------------
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision. You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = version1.split(".")
        versions2 = version2.split(".")
        for i in range(max(len(versions1),len(versions2))):
            v1 = int(versions1[i]) if i < len(versions1) else 0
            v2 = int(versions2[i]) if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 <v2:
                return -1
        return 0

"""
Runtime: 28 ms, faster than 60.82% of Python online submissions for Compare Version Numbers.
Memory Usage: 12.6 MB, less than 91.84% of Python online submissions for Compare Version Numbers.
"""