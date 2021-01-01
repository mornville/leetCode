"""
938. Range Sum of BST
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val >= low and root.val <= high:
                self.sum+=root.val
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
        return self.sum

"""
Runtime: 268 ms, faster than 26.43% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.3 MB, less than 28.17% of Python3 online submissions for Range Sum of BST.
"""