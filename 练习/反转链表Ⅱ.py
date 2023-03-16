# Definition for singly-linked list.
from typing import List, Optional


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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 哨兵节点 dummy
        p0 = dummy = ListNode(next=head)
        for _ in range(left-1):
            p0 = p0.next

        pre = None
        cur = p0.next
        # 控制范围的链表迭代
        for _ in range(right-left+1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        p0.next.next = cur
        p0.next = pre

        return dummy.next


head = [1,2,3,4,5]
left = 2
right = 4
solution = Solution()
head = solution.crate_ListNode(head)
print(solution.reverseBetween(head,left,right))