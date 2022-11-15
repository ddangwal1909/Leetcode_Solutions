# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q=[]
        if root is None:
            return []
        q.append(root)
        res=[]
        while len(q)>0:
            tmp_q=[]
            curr=[]
            while len(q)>0:
                ele=q.pop(0)
                curr.append(ele.val)
                if ele.left:
                    tmp_q.append(ele.left)
                if ele.right:
                    tmp_q.append(ele.right)
            res.append(curr)
            q=tmp_q
        
        return res
    
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=self.levelOrder(root)
        return res[::-1]