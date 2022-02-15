# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res=[]
        
        def inorder(root):
            nonlocal res
            if len(res)>k:
                return
            if root.left:
                inorder(root.left)
            res.append(root.val)
            #print(res)
            if root.right:
                inorder(root.right)
            return
        
        inorder(root)
        return res[k-1]