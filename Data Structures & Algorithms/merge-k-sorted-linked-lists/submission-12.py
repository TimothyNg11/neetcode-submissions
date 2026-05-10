# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while any([lists[x] for x in range(len(lists))]):
            
            lst = [(x.val, x) for x in lists if x is not None]
            minLst = min(lst, key=lambda x: x[0])

            for i,l in enumerate(lists):
                if minLst[1] == l:
                    curr.next = l
                    curr = curr.next
                    lists[i] = l.next
        
        curr.next = None
        return head.next

