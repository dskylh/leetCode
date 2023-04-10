from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head is not None:
            l.append(head)
            head = head.next
        return l[int(len(l) / 2)]
