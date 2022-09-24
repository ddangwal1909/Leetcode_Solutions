"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        result=[]
        def postorder_helper(currnode):
            nonlocal result
            if currnode is None:
                return
            
            else:
                if currnode.children:
                    for i in currnode.children:
                        postorder_helper(i)
                    result.append(currnode.val)
                else:
                    result.append(currnode.val)
            return
        
        postorder_helper(root)
        
        return result
                    
                
                