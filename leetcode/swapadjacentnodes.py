# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        temp=ListNode()
        if head==None:
            return None
        if head.val==1 and head.next==None:
            return head
        returnNode=None
        flag=0

        node1=node
        node2=node.next
        tail=node.next.next
        node1.next=tail
        node2.next=node1
        returnNode=node2
        
        while node2 and node2.next and node2.next.next:
            tail=None
            if node1.next.next.next:
                tail=node1.next.next.next
            temp=node1.next
            
            node1.next=node1.next.next
            temp.next=None
            node1.next.next=temp
            node1=node1.next.next
            node2=node2.next.next
            if tail:
                node1.next=tail
            

        return returnNode

            

            