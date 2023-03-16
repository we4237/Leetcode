# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        cur = slow
        while cur :
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        while pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True

    def create_ListNode(self,li:list):
        head = ListNode(li[0])
        tail = head

        for element in li[1:]:
            node = ListNode(element)
            tail.next = node
            tail = node

        return head

head = [1,2,2,1]
solution = Solution()
head = solution.create_ListNode(head)
print(solution.isPalindrome(head))