# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        res = ListNode()
        a = res
        dct = {}
        while curr:
            counter = 0
            for i in range(k):
                if not curr:
                    for j in range(i):
                        res.next = ListNode(dct[j])
                        res = res.next
                    return a.next
                dct[i] = curr.val
                curr = curr.next
                counter = i
            
            while counter >= 0:
                res.next = ListNode(dct[counter])
                counter -= 1
                res = res.next
            
            dct.clear()
        
        return a.next
        