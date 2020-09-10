"""
925. Long Pressed Name
----------------------

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed. 

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        p1 = 0
        p2 = 0
        
        while p1 < len(name) and p2 < len(typed):
            if name[p1] == typed[p2]:
                p1 +=1
                p2+=1
            elif p2>=1 and typed[p2] == typed[p2-1]:
                p2+=1
            else:
                return False
        
        if p1!=len(name):
            return False
        else:
            while p2<len(typed):
                if typed[p2] != typed[p2-1]:
                    return False
                p2+=1
                
        return True
                    
"""
Runtime: 8 ms, faster than 99.66% of Python online submissions for Long Pressed Name.
Memory Usage: 12.7 MB, less than 69.86% of Python online submissions for Long Pressed Name.
"""