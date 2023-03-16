# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next


        p0 = dummy = ListNode(next=head)
        pre = None
        cur = p0.next
        while cnt>=2:
            cnt -= 2

            for _ in range(2):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            tmp = p0.next
            p0.next.next = cur
            p0.next = pre
            cur = tmp
        return dummy.next
