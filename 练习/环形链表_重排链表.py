# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # "链表的中间节点" + "反转链表"
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        pre = None
        cur = mid
        while(cur):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        head2 = pre
        while head2.next:
            # 预先存储
            nxt = head.next
            nxt2 = head2.next

            # 指向
            head.next = head2
            head2.next = nxt

            # 存储
            head = nxt
            head2 = nxt2

    def create_ListNode(self, Li: list):
        h = ListNode(val=Li[0])
        tail = h

        for elm in Li[1:]:
            node = ListNode(elm)
            tail.next = node
            tail = node
        return h

head = [1,2,3,4,5]
solution = Solution()
head = solution.create_ListNode(head)
solution.reorderList(head)