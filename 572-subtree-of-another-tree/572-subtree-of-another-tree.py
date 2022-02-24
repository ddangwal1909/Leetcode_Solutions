# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def dfs(self,root,subRoot):
        
        if root is None and subRoot is None:
            return True
        elif (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.dfs(root.left,subRoot.left) and self.dfs(root.right,subRoot.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = []
        
        queue.append(root)
        
        while queue :
            
            tmp_queue = []
            
            while queue:
                curr = queue.pop(0)
                
                if curr.val == subRoot.val:
                    if self.dfs(curr,subRoot):
                        return True
                
                if curr.left:
                    tmp_queue.append(curr.left)
                
                if curr.right:
                    tmp_queue.append(curr.right)
            
            queue = tmp_queue
        
        return False
            
        