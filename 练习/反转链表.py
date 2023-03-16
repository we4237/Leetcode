# Definition for singly-linked list.
import sys
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def create_ListNode(self,li:list):
        head = ListNode(li[0])
        tail = head

        for element in li[1:]:
            node = ListNode(element)
            tail.next = node
            tail = node

        return head

# 迭代
    # def reverseList(self, head: Optional[ListNode]) -> ListNode:
    #     pre = None
    #     cur = head
    #     while cur:
    #         nxt = cur.next
    #         # # 反转
    #         # cur.next = pre
    #         pre = cur
    #         cur = nxt
    #
    #     return pre

    # def reverseList(self, head: Optional[ListNode]) -> ListNode:
    #     stack = deque(  )
    #
    #     while(head):
    #         stack.append(head)
    #         head = head.next
    #
    #     dummy = ListNode()
    #     cur = dummy
    #     while(stack):
    #         cur.next = ListNode(st)
    #     dummy.next = None
    #     return cur.next

    # 迭代
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        pre = None
        cur = head
        while(cur):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 递归(抽象)
    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        if head == None or head.next == None:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

solution = Solution()
head = solution.create_ListNode([1,2,3,4,5])
print(solution.reverseList(head))
