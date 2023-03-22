# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former,later = head,head
        for _ in range(k):
            former = former.next

        while former:
            former,later = former.next,later.next
        # 删掉later前K个节点
        return later
