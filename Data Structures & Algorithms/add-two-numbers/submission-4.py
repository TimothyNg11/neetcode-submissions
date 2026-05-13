# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        lst1 = []
        while curr:
            lst1.append(curr.val)
            curr = curr.next
        curr2 = l2
        lst2 = []
        while curr2:
            lst2.append(curr2.val)
            curr2 = curr2.next
        
        a = lst1[::-1]
        b = lst2[::-1]
        num = [str(x) for x in a]
        c = int("".join(num))
        num2 = [str(x) for x in b]
        d = int("".join(num2))
        newStr = str(c + d)
        lstnode = ListNode(0)
        cur = lstnode
        for charr in reversed(newStr):
            cur.next = ListNode(int(charr))
            cur = cur.next
        cur.next = None

        return lstnode.next
        