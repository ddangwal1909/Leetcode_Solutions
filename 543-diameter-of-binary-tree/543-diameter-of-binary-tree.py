# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        global_mx=0
        
        def helper (root1):
            nonlocal global_mx
            if not root1:
                return 0
            
            r=helper(root1.right)
            l=helper(root1.left)
            global_mx =  max(r+l,global_mx)
            return max(l,r)+1
        
        helper(root)
        
        return global_mx