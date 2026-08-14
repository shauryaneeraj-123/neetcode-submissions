# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BASE CASE: If node is empty, stop and return None
        if root is None:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # RECURSIVE CALL: Notice the `self.` prefix!
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the modified root node
        return root