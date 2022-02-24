# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def dfs(self,root,subRoot):
        
        if root is None and subRoot is None:
            ## matched till the end from root of both trees
            return True
        
        elif (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        elif root.val != subRoot.val:
            return False
        else:
            ## check if both and left and right match the conditions
            return self.dfs(root.left,subRoot.left) and self.dfs(root.right,subRoot.right)
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = []
        
        queue.append(root)
        
        ## start Level Order BFS here
        while queue :
            
            tmp_queue = []
            
            while queue:
                curr = queue.pop(0)
                if curr.val == subRoot.val:
                    ## if did not find this time, try for next matched value of root.val
                    if self.dfs(curr,subRoot):
                        return True
                
                if curr.left:
                    tmp_queue.append(curr.left)
                
                if curr.right:
                    tmp_queue.append(curr.right)
            
            queue = tmp_queue
        
        ## even after all traversals the subtree wasnt found
        return False
            
        