# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashtable={}
        
        curr_head=headA
        while curr_head:
            hashtable[curr_head]=1
            curr_head=curr_head.next
        
        curr_head=headB
        while curr_head:
            if curr_head in hashtable.keys():
                return curr_head
            else:
                curr_head=curr_head.next
        return None