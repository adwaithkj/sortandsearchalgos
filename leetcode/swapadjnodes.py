# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead=None
        temphead=head

        while temphead!=None:
            temp=temphead.next
            if newhead==None:
                newhead=temp
            else:
                newhead.next=temp
            temphead=temphead.next.next
1,2,3,4
2,
