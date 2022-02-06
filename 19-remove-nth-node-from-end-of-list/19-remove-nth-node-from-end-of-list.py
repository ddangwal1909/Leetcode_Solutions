# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def findlen(self,head):
        cnt=0
        while head:
            head=head.next
            cnt+=1
        return cnt
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        l = self.findlen(head)
        
        if l==1:
            return None
        elif l-n==0:
            head=head.next
            return head
            
            
        else:
            headtmp=head

            for i in range(l-n):
                prev=headtmp
                headtmp=headtmp.next

            prev.next=headtmp.next

            return head