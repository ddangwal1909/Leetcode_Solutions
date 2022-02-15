# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stck = []
        while root is not None:
            self.stck.append(root)
            root=root.left
            
    def next(self) -> int:
        curr = self.stck.pop(-1)
        curr1=curr.right
        while curr1 is not None:
            self.stck.append(curr1)
            curr1=curr1.left
        return curr.val
        

    def hasNext(self) -> bool:
        if not self.stck:
            return False
        else:
            return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()