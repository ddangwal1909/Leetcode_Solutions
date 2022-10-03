# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        hashmap={}
        hashmap[x]=[-1,0]
        hashmap[y]=[-1,0]
        
        
        def helper(root,curr_depth,parent):
            curr_depth+=1
            if hashmap[x][0]!=-1 and hashmap[y][0]!=-1:
                return
            if root.val==x:
                hashmap[x][0]=curr_depth
                hashmap[x][1]=parent.val
            if root.val==y:
                hashmap[y][0]=curr_depth
                hashmap[y][1]=parent.val
            if root.left:
                helper(root.left,curr_depth,root)
            if root.right:
                helper(root.right,curr_depth,root)
            return
        
        helper(root,0,root)
        if hashmap[x][0]==hashmap[y][0] and hashmap[y][1]!=hashmap[x][1]:
            return True
        else:
            return False
        
        