# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BASE CASE: Empty node has depth 0
        if root is None:
            return 0
        
        # Get max depth of left subtree recursively (using self.)
        left_depth = self.maxDepth(root.left)
        
        # Get max depth of right subtree recursively (using self.)
        right_depth = self.maxDepth(root.right)
        
        # Add 1 (for current node) to max depth among children
        return 1 + max(left_depth, right_depth)