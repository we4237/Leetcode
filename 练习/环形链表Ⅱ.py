# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow is fast:
        #         break
        # if not (fast and fast.next):
        #     return
        # fast = head
        # while fast != slow:
        #     fast = fast.next
        #     slow = slow.next
        # return fast

        # 茶神
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow is fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next

                return slow
        return None
