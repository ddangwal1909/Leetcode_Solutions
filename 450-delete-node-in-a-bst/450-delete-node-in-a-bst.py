# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def predecessor(self,root):
        # on left then all right
        root=root.left
        while root.right:
            root=root.right
        return root.val
    
    def successor(self,root):
        # one right and then all left
        root = root.right
        
        while root.left:
            root=root.left
        return root.val
    
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            root=None
            return None
        
        # leaf node
        elif not (root.left or root.right) and root.val == key:
            root=None
            return None
        
        elif root.val>key:
            root.left = self.deleteNode(root.left,key)
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        
        ## found the node with key
        else:
            
            if root.right:
                root.val=self.successor(root)
                root.right = self.deleteNode(root.right,root.val)
            else:
                root.val=self.predecessor(root)
                root.left=self.deleteNode(root.left,root.val)
        return root
            
        
            