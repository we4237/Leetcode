from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret =[]
        if not root:
            return ret

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            ret.append(node.val)
            stack.extend(node.children)

        return ret[::-1]