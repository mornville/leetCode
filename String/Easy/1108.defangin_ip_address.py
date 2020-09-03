"""
1108. Defanging an IP Address
-----------------------------
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')

"""
Runtime: 20 ms, faster than 61.67% of Python online submissions for Defanging an IP Address.
Memory Usage: 12.6 MB, less than 94.15% of Python online submissions for Defanging an IP Address.
"""