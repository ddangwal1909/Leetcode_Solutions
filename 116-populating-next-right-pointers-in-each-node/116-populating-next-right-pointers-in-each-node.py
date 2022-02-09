"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        
        queue=[]
        res=Node()
        queue.append(root)
        head=res
        
        if not root:
            return root
        
        while queue:
            tmp_q=[]
            for i in queue:
                curr=i
                if curr.left:
                    tmp_q.append(curr.left)        
                if curr.right:
                    tmp_q.append(curr.right)
                res.next=Node(curr.val)
                res=res.next
            if tmp_q:
                res.next=Node('#')
                res=res.next
            queue=[]
            queue = tmp_q
            
        
        return head.next
        