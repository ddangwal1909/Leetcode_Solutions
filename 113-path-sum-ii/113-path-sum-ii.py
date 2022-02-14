# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        res=[]
        
        def helper(root,sm,target,queue_curr):
            
            nonlocal res
            if root is None:
                return
            if sm+root.val==target:
                queue_curr.append(root.val)
                print(queue_curr)
                if root.left is None and root.right is None:  
                    res.append(queue_curr)
                queue_curr.pop()
            sm+=root.val
            queue_curr.append(root.val)
            if root.left:
                helper(root.left,sm,target,queue_curr[:])
            if root.right:
                helper(root.right,sm,target,queue_curr[:])
            return
        
        
        helper(root,0,targetSum,[])
        return res
        
                    