class Node: # 链表
    def __init__(self,key="",count=0):
        self.prev = None # 指向上一个节点的指针prev
        self.next = None # 指向下一个节点的指针next
        self.keys = {key}
        self.count = count


    def insert(self, node:'Node') -> 'Node':  # 在 self 后插入 node
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self): # 从链表中移除self
        self.prev.next = self.next
        self.next.prev = self.prev



class AllOne:
# 每次操作的时间复杂度均为 O(1)O(1)--双向链表和哈希表
    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root # 初始化链表哨兵,下面判断节点的next若为self.root,则表示next为空(prev同理)
        self.nodes = {}

    def inc(self,key:str) -> None:
        if key not in self.nodes: # key不在链表中
            if self.root.next is self.root or self.root.next.count>1:
                self.nodes[key] = self.root.insert(Node(key,1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else: #key在链表中
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count>cur.count+1:
                self.nodes[key] = cur.insert (Node(key,cur.count+1))
            else:
                nxt.keys.add(key)
                self.nodes[key]=nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0:
                cur.remove()


    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1: # key仅出现一次,将其移除nodes
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.root or pre.count <cur.count-1:
                self.nodes[key] = cur.prev.insert(Node(key,cur.count-1))
            else:
                pre.keys.add(key)
                self.nodes[key]=pre
        cur.keys.remove(key)
        if len(cur.keys)==0:
            cur.remove()




    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else""

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()