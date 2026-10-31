# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        res = ListNode()
        a = res
        while head1 and head2:
            if head1.val >= head2.val:
                res.next = ListNode(head2.val)
                head2 = head2.next
            else:
                res.next = ListNode(head1.val)
                head1 = head1.next
            res = res.next
        
        while head1:
            res.next = ListNode(head1.val)
            head1 = head1.next
            res = res.next
        
        while head2:
            res.next = ListNode(head2.val)
            head2 = head2.next
            res = res.next
        
        return a.next
        
        
        