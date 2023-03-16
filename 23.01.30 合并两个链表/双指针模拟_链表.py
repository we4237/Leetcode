# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p = q = list1
        for _ in range(0,a-1): # 指针p指向链表list1中第a个节点的前一个节点
            p = p.next
        for _ in range(b): # 指针q指向链表list1中第b个节点
            q = q.next
        p.next = list2
        while p.next:
            p = p.next
        p.next = q.next
        q.next = None

        return list1

# list1 = [ListNode(val=0,next=1),
#          ListNode(val=1,next=2),
#          ListNode(val=2,next=3),
#          ListNode(val=3,next=4),
#          ListNode(val=4,next=5),
#          ListNode(val=5,next=6)]
list1 = [0,1,2,3,4,5,6]
a=2
b=5
# list2 = [ListNode(val=1000000,next=1000001),
#          ListNode(val=1000001,next=1000002),
#          ListNode(val=1000002,next=1000003),
#          ListNode(val=1000003,next=1000004)]
list2 = [1000000,1000001,1000002,1000003,1000004]
solution = Solution()
print(solution.mergeInBetween(list1,a,b,list2))