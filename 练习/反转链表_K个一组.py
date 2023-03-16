# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def crate_ListNode(selfself,li:List):
        head = ListNode(li[0])
        tail = head
        for element in li[1:]:
            node = ListNode(element)
            tail.next = node
            tail = node

        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        p0 = dummy = ListNode(next=head)
        pre = None
        cur = p0.next
        while cnt >= k:
            cnt -= k

            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

 
head = [1,2,3,4,5]
k = 2
solution = Solution()
head = solution.crate_ListNode(head)
print(solution.reverseKGroup(head,k))