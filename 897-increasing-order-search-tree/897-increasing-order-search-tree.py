# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        stack=[]
        newroot=TreeNode(0)
        curr_root=newroot
        curr=root
        
        while True:
            if curr is not None:
                stack.append(curr)
                curr=curr.left
                    
            elif len(stack)>0:
                curr_pop=stack.pop()
                curr_root.right=TreeNode(curr_pop.val)
                curr_root=curr_root.right
                curr=curr_pop.right
            else:
                break
            #print(stack)
        return newroot.right
                
                
                
                
            
            