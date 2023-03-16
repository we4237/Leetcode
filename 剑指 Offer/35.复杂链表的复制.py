
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from collections import defaultdict


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None :
            return
        dic = defaultdict()
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head

        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        return dic[head]
