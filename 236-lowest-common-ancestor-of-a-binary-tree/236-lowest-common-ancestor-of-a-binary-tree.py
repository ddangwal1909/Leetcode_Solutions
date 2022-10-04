# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res=None
        def helper(root):
            nonlocal res
            if root is None:
                return False
            else:
                curr= root==p or root==q
                left=helper(root.left)
                right=helper(root.right)                
                
                if int(curr)+int(left)+int(right)>=2:
                    res=root
                return curr or left or right
        
        helper(root)
        return res
                
                    
                    