# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def findlen(self,headtmp):
        cnt=0
        while headtmp:
            headtmp=headtmp.next
            cnt+=1
            
        return cnt
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l=self.findlen(head)
        mid=(l//2)
        
        headtmp=head
        for i in range(mid):
            headtmp=headtmp.next
        
        return headtmp
        
        
        