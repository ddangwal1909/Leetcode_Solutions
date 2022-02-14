# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]
        
        queue=[]
        queue.append(root)
        
        cnt=0
        
        if root is None:
            return []
        
        while queue:
            tmp_queue=[]
            tmp_res=[]
            while queue:
                curr_root=queue.pop(0)
                tmp_res.append(curr_root.val)
                if curr_root.left:
                    tmp_queue.append(curr_root.left)
                if curr_root.right:
                    tmp_queue.append(curr_root.right)
            queue=tmp_queue
            if cnt%2==0:
                res.append(tmp_res)
            else:
                res.append(tmp_res[::-1])
            cnt+=1
        
        return res
            
            
                    
        
        