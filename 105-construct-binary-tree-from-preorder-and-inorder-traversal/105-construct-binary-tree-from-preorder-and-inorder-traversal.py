# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        
        def helper(i,j):
            nonlocal idx
            if i>j:
                return None
            else:
                
                root=TreeNode(preorder[idx])
                value=preorder[idx]
                idx+=1
                root.left = helper(i,inorder.index(value)-1)
                root.right = helper(inorder.index(value)+1,j)
                
                return root
        
        idx=0
        
        main_root=helper(0,len(preorder)-1)
        return main_root
        