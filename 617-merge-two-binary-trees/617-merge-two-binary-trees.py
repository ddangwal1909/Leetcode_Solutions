# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def helper(root_1=None,root_2=None):
            ## current_value
            root_tmp=TreeNode()
            if root_1 is None and root_2 is not None:
                root_tmp.val = root_2.val
            elif root_1 is not None and root_2 is None:
                root_tmp.val = root_1.val
            elif root_1 is not None and root_2 is not None:
                root_tmp.val = root_1.val + root_2.val
            else:
                root_tmp=None
            ## add left child
            if root_1 is None and root_2 is not None:
                root_tmp.left = helper(None,root_2.left)
                root_tmp.right = helper(None, root_2.right)
            elif root_1 is not None and root_2 is None:
                root_tmp.left = helper(root_1.left,None)
                root_tmp.right = helper(root_1.right, None)
            elif root_1 is not None and root_2 is not None:
                root_tmp.left = helper(root_1.left,root_2.left)
                root_tmp.right = helper(root_1.right, root_2.right)
            else:
                return None
                
            return root_tmp
            
        
        root = helper(root1,root2)
        
        return root
        
            