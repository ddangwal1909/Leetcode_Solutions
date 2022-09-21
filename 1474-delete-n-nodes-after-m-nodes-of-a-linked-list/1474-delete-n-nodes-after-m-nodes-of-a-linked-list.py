# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        curr_m=m
        curr_n=n
        curr=head
        while curr:
            for i in range(curr_m-1):
                if curr is None:
                    return head
                else:
                    curr=curr.next
            
            #print('prev:',curr.val)
            prev=curr
            for j in range(curr_n+1):
                if curr is None:
                    if prev is None:
                        return head
                    else:
                        prev.next=None
                        return head
                else:
                    curr=curr.next
                    
            #print('next:',curr.val)
            prev.next=curr
            curr_m=m
            curr_n=n
        
        return head
            
            
            
                
                