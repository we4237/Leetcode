
# 直接遍历
# class MyCalendar:
#
#     def __init__(self):
#         self.booked = []
#
#     def book(self, start: int, end: int) -> bool:
#         if any(r > start and l < end for l,r in self.booked):
#             return False
#
#         self.booked.append((start,end))
#         return True


# from sortedcontainers import SortedDict
#
# 二分查找
# class MyCalendar:
#
#     def __init__(self):
#         self.booked = SortedDict()
#
#     def book(self, start: int, end: int) -> bool:
#         i = self.booked.bisect_left(end)
#         if i == 0 :
#
#
#             self.booked[start] = end
#
#             return True
#         if self.booked.items()[i - 1][1] <= start:
#             a = self.booked.items()[i - 1]
#             print('a:'.format(a))
#
#             b = self.booked.items()[i - 1][1]
#             print('b'.format(b))
#             self.booked[start] = end
#             return True
#         return False

# 线段树
class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self,start:int,end:int,l:int,r:int,idx:int) -> bool:
        if r < start or end < l:
            return False
        if idx in self.lazy: # 如果该区间已被预定,则直接返回
            return True
        if start <= l and r <= end:
            return idx in self.tree # 在区间内
        mid = (1+r)//2
        return self.query(start,end,l,mid,2*idx) or \
                self.query(start,end,mid+1,r,2*idx + 1)

    def update(self,start:int,end:int,l:int,r:int,idx:int) -> None:


        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree.add(idx)
            self.lazy.add(idx)


        else:
            mid = (1+r)//2
            self.update(start,end,l,mid,2*idx)
            self.update(start,end,mid+1,r,2*idx+1)
            self.tree.add(idx)
            if 2 * idx in self.lazy and 2 * idx + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10,20)
# print(param_1)
param_1 = obj.book(15,25)
# print(param_1)
param_1 = obj.book(20,30)