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
    def connect(self, root: 'Node') -> 'Node':
        
        queue = []
        prev=root
        curr=root
        queue.append(curr)
        
        if root is None:
            return root
        
        while queue:
            
            tmp_queue=[]
            
            curr = queue[0]
            for i in range(1,len(queue)):
                print(queue[i].val)
                curr.next = queue[i]
                curr=curr.next
            
            curr=Node('#')
                
            while queue:
                tmp = queue.pop(0)
                if tmp.left:
                    tmp_queue.append(tmp.left)
                if tmp.right:
                    tmp_queue.append(tmp.right)
            
            queue = tmp_queue
        
        return root
            
            
                