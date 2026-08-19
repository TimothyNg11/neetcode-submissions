"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = Node(0)
        a = res
        b = res
        curr = head
        curr2 = head
        dct = {None: None}

        while curr:
            res.next = Node(curr.val, curr.next, None)
            dct[curr] = res.next
            res = res.next
            curr = curr.next
        
        while curr2:
            b.next.random = dct[curr2.random]
            b = b.next
            curr2 = curr2.next


        return a.next

        