"""
144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.ans.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            
        return self.ans 
            
"""
Runtime: 24 ms, faster than 95.20% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 14.1 MB, less than 61.00% of Python3 online submissions for Binary Tree Preorder Traversal.
"""